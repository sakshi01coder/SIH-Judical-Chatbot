<?php
// Include database connection file
require 'db_connect.php';

// Check if form is submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get form data and sanitize
    $firstName = htmlspecialchars($_POST['firstName']);
    $lastName = htmlspecialchars($_POST['lastName']);
    $title = htmlspecialchars($_POST['title']);
    $description = htmlspecialchars($_POST['description']);

    // Prepare SQL query
    $sql = "INSERT INTO form_submissions (first_name, last_name, title, description) VALUES (:firstName, :lastName, :title, :description)";

    try {
        // Prepare statement
        $stmt = $pdo->prepare($sql);
        
        // Bind parameters
        $stmt->bindParam(':firstName', $firstName);
        $stmt->bindParam(':lastName', $lastName);
        $stmt->bindParam(':title', $title);
        $stmt->bindParam(':description', $description);
        
        // Execute the statement
        $stmt->execute();
        
        // Success message
        echo 'Your query has been submitted successfully.';
    } catch (PDOException $e) {
        echo 'Error: ' . $e->getMessage();
    }
} else {
    echo 'Invalid request method.';
}
?>
