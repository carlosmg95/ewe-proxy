<?php

$url = $_POST['url'];
$key = $_POST['key'];
$format = $_POST['format'];

$filename = 'performers/playVideo.py';
$f = fopen($filename, 'r');
$txt = fread($f, filesize($filename));
fclose($f);

$_SLN = "\r\n";
$txt = explode($_SLN, $txt);
$pre = ''; $post = '';

$exists = false;
foreach ($txt as $dir) {
    if (!preg_match('/else:/', $dir)) {
        if (!$exists)
            $pre .= $dir . $_SLN;
        else
            $post .= $dir . $_SLN;
    } else {
        $exists = true;
    }
}

if ($exists) {
    $f = fopen($filename, 'w');
    fwrite($f, $pre);
    fwrite($f, 'elif \'' . $key . '\' in sys.argv:' . $_SLN);
    fwrite($f, '    cast.play_media((\'' . $url . '\'), \'video/' . $format . '\')' . $_SLN);
    fwrite($f, 'else:' . $_SLN);
    fwrite($f, $post);
    fclose($f);
}