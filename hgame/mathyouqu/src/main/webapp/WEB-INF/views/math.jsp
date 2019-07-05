<%@ page contentType="text/html;charset=UTF-8" language="java" pageEncoding="utf-8" isELIgnored="false" %>
<html>
<head>
    <title>Title</title>
</head>
<body>
<p>${message}</p>
<br/>
<form action="/index.php" method="post">
    Your Answer: <input type="text" name="answer" />
    <input type="submit" value="Submit" />
</form>
</body>
</html>
