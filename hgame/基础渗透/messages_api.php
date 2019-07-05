 
 <?php
require_once('functions.php');
if ($_GET['action'] === 'add') {
    if (!isset($_POST['new_message']) or !isset($_POST['token'])) {
        header("Location: /index.php");
    } else {
        add_message(htmlspecialchars(addslashes($_POST['new_message'])));
    }
} elseif ($_GET['action'] === 'delete') {
    if (!isset($_POST['message_id']) or !isset($_POST['token'])) {
        header("Location: /index.php");
    } else {
        delete_message(addslashes($_POST['message_id']));
    }
} elseif ($_GET['action'] === 'get_new') {
    if (is_null($_SESSION['user_id'])) {
        http_response_code(403);
    } else {
        echo get_new_messages();
    }
} elseif
($_GET['action'] === 'get') {
    if (is_null($_SESSION['user_id'])) {
        http_response_code(403);
    } else {
        echo get_messages();
    }
}