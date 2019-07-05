<?php
//ini_set("display_errors", "on");
require_once('config.php');
session_start();

function sql_query($sql_query)
{
    global $mysqli;
    $res = $mysqli->query($sql_query);
    return $res;
}

function csrf_token()
{
    $token = '';
    $chars = str_split('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');
    for ($i = 0; $i < 48; $i++) {
        $token = $token . $chars[random_int(0, 61)];
    }
    $_SESSION['token'] = $token;
    echo "<input type='hidden' value='$token' id='token'>";
}

function res_to_json($res, $type)
{
    $json['type'] = $type;
    $json['status'] = "true";
    $json["content"] = array();
    foreach ($res as $message) {

        $array_tmp['user_id'] = $message['user_id'];
        $array_tmp['user'] = $message['user'];
        $array_tmp['avatar'] = get_avatar($message['user_id']) != null ? get_avatar($message['user_id'])['content'] : md5($message['user']);
        $array_tmp['message'] = $message['content'];
        $array_tmp['message_id'] = $message['message_id'];
        $array_tmp['time'] = $message['date'];
        array_push($json["content"], $array_tmp);
    }
    $json["content"] = $json["content"];
    return json_encode($json);
}

function judge($username, $password)
{
    if ($username == null) {
        echo "username's length error!";
        return false;
    } elseif (strlen($password) < 6 or strlen($password) > 16) {
        echo "password's length error!";
        return false;
    } else {
        return true;
    }
}

function register($username, $password, $token)
{
    if (judge($username, $password) == 1 and $token === $_SESSION['token']) {
        $password = md5($password);
        $sql_query = "insert into `users`(`username`,`password`) VALUES ('$username','$password')";
        $res = sql_query($sql_query);
        if ($res) {
            echo 'register success!';
        } else {
            echo 'error!';
        }
    } else {
        echo "error!";
        return false;
    }

}

function login($username, $password, $token)
{
    if (!isset($_SESSION['login']) and $token === $_SESSION['token']) {
        $password = md5($password);
        $sql_query = "select * from `users` where `username`='$username' and `password`='$password'";
        $res = sql_query($sql_query);
        if ($res->num_rows) {
            $data = $res->fetch_array();
            $_SESSION['user_id'] = $data['user_id'];
            $_SESSION['user'] = $data['username'];
            $_SESSION['groups'] = $data['groups'];
            $_SESSION['login'] = 1;
            setcookie('user', $_SESSION['user']);
            setcookie('groups', $_SESSION['groups']);
        } else {
            echo "error!";
            return false;
        }
    } else {
        echo "error!";
        return false;
    }
}

function loginout()
{
    if ($_GET['loginout'] === $_SESSION['token']) {
        session_destroy();
        setcookie('groups', null);
        setcookie('user', null);
        Header("Location: index.php");
    }
}

function get_avatar($user_id)
{
    $sql_query = "select `avatar` from `users` where `user_id`=$user_id";
    $res = sql_query($sql_query)->fetch_row()[0];
    if ($res) {
        return array('name' => $res, 'content' => base64_encode(file_get_contents('./img/avatar/' . $res . '.png')));
    } else {
        return null;
    }
}

function get_new_messages()
{
    $start = $_GET['start'] ?? 0;
    $start = addslashes($start);
    $user_id = $_SESSION['user_id'];
    $sql_query = "select * from `messages` where `user_id`=$user_id LIMIT $start,999999999999";
    $res = sql_query($sql_query);
    if ($res->num_rows) {
        return res_to_json($res, "messages");
    }

}

function get_messages()
{
    $start = $_GET['start'] ?? 0;
    $start = addslashes($start);
    $user_id = $_SESSION['user_id'];
    $sql_query = "select * from `messages` where `user_id`=$user_id ORDER BY `message_id` DESC LIMIT $start,12";
    $res = sql_query($sql_query);
    if ($res->num_rows) {
        return res_to_json($res, "messages");
    }
}

function add_message($message)  //action=add
{
    if ($_POST['token'] === $_SESSION['token']) {
        if (isset($_SESSION['login']) and mb_strlen($message) > 6) {
            $user_id = $_SESSION['user_id'];
            $user = $_SESSION['user'];
            $sql_query = "insert into `messages`(`user_id`,`user`,`content`) VALUES($user_id,'$user','$message')";
            sql_query($sql_query);
        } elseif (!isset($_SESSION['login'])) {
            echo "login error";
        } else {
            echo "length error";
        }
    }
}

function delete_message($message_id)
{
    $user_id = $_SESSION['user_id'];
    if ($_POST['token'] === $_SESSION['token']) {
        if ($_SESSION['groups'] == 0) {
            $sql_query = "delete from `messages` where `message_id`=$message_id and `user_id`=$user_id";
        } elseif ($_SESSION['groups'] == 1) {
            $sql_query = "delete from `messages` where `message_id`=$message_id";
        }
        sql_query($sql_query);

    }
}

function rand_filename()
{
    $tmp = `cat /dev/urandom | head -n 10 | md5sum | head -c 15`;
    $sql_query = "select `avatar` from `users` where `avatar`=$tmp";
    $res = sql_query($sql_query);
    if ($res->num_rows) {
        return rand_filename();
    } else {
        return $tmp;
    }
}

function upload_avatar()    //action=uploadavatar
{
    $type = $_FILES['file']['type'];
    $user_id = $_SESSION['user_id'];
    if ($type == 'image/gif' || $type == 'image/jpeg' || $type == 'image/png') {
        $avatar = get_avatar($user_id);
        if ($avatar == null) {
            $name = rand_filename();
            move_uploaded_file($_FILES['file']['tmp_name'], "./img/avatar/" . $name . ".png");
            $sql_query = "update `users` set `avatar`='$name' WHERE `user_id`=$user_id";
            sql_query($sql_query);
        } else {
            move_uploaded_file($_FILES['file']['tmp_name'], "./img/avatar/" . $avatar['name'] . ".png");

        }
    }
}

function change_password($opassword, $npassword, $npasswod_again)
{
    if (judge($_SESSION['user'], $npassword)) {
        if ($npasswod_again !== $npassword) {
            echo "difference error";
        } else {
            $user_id = $_SESSION['user_id'];
            $sql_query = "select `password` from `users` where `user_id`=$user_id";
            $res = sql_query($sql_query);
            if ($res->num_rows) {
                if ($res->fetch_row()[0] === md5($opassword)) {
                    $sql_query = "update `users` set `password`=md5($npassword) WHERE `user_id`=$user_id";
                    $res = sql_query($sql_query);
                    echo $res;
                    echo "successful";
                } else {
                    echo "oldpassword error";
                }
            }
        }

    }

}