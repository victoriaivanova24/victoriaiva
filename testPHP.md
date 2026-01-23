<?php
//JSON
header("Content-Type: application/json; charset=UTF-8");

//Mistakes 
ini_set('display_errors', 1);
error_reporting(E_ALL);

//SQLite with PDO 
try {
    $pdo = new PDO('sqlite:tasks.sqlite');
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
} catch (PDOException $e) {
    http_response_code(500);
    echo json_encode(["message" => "Connection error: " . $e->getMessage()]);
    exit();
}

//HTTP-method
$method = $_SERVER['REQUEST_METHOD'];
$request_uri = $_SERVER['REQUEST_URI'];
$uri_parts = explode('/', trim($request_uri, '/'));
$resource = $uri_parts[count($uri_parts) - 1];

//URL in /api.php/tasks or /api.php/tasks/ID
if ($resource !== 'tasks') {
    http_response_code(404);
    echo json_encode(["message" => "Resource not found"]);
    exit();
}

//body of POST/PUT
$input = json_decode(file_get_contents("php://input"), true);

switch ($method) {
    case 'GET':
        $id = isset($uri_parts[count($uri_parts) - 2]) && is_numeric($uri_parts[count($uri_parts) - 2]) ? $uri_parts[count($uri_parts) - 2] : null;

        if ($id) {
            $stmt = $pdo->prepare("SELECT * FROM tasks WHERE id = ?");
            $stmt->execute([$id]);
            $task = $stmt->fetch(PDO::FETCH_ASSOC);
            if ($task) {
                echo json_encode($task);
            } else {
                http_response_code(404);
                echo json_encode(["message" => "Task not found"]);
            }
        } else {
            $stmt = $pdo->query("SELECT * FROM tasks ORDER BY created_at DESC");
            $tasks = $stmt->fetchAll(PDO::FETCH_ASSOC);
            echo json_encode($tasks);
        }
        break;

    case 'POST':
        // Создание задачи: POST /tasks (поля: title, description, status)
        if (!isset($input['title']) || empty($input['title'])) {
            http_response_code(400);
            echo json_encode(["message" => "Title is required"]);
            break;
        }

        $stmt = $pdo->prepare("INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)");
        $stmt->execute([
            $input['title'],
            $input['description'] ?? null,
            $input['status'] ?? 'pending'
        ]);
        
        $id = $pdo->lastInsertId();
        $stmt = $pdo->prepare("SELECT * FROM tasks WHERE id = ?");
        $stmt->execute([$id]);
        $newTask = $stmt->fetch(PDO::FETCH_ASSOC);
        
        http_response_code(201);
        echo json_encode($newTask);
        break;

    case 'PUT':
        $id = $uri_parts[count($uri_parts) - 2];
        if (!is_numeric($id)) {
             http_response_code(400);
             echo json_encode(["message" => "Invalid task ID"]);
             break;
        }

        $stmt = $pdo->prepare("SELECT * FROM tasks WHERE id = ?");
        $stmt->execute([$id]);
        $task = $stmt->fetch(PDO::FETCH_ASSOC);

        if (!$task) {
            http_response_code(404);
            echo json_encode(["message" => "Task not found"]);
            break;
        }
        
        if (isset($input['title']) && empty($input['title'])) {
            http_response_code(400);
            echo json_encode(["message" => "Title cannot be empty"]);
            break;
        }
