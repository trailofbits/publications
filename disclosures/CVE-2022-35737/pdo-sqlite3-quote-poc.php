<?php
ini_set('memory_limit', '16G');
$conn = new PDO('sqlite:./placeholder.sql3');
$conn->quote(str_repeat("a", intdiv(0x100000001 - 3 , 2)));

