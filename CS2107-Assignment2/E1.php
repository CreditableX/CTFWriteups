<?php
function readFileContent($url) {
    $content = file_get_contents($url);

    // If the content contains "CS2107", block the response
    if (strpos($content, 'CS2107') !== false) {
        return "Hacker detected!!";
    }

    return $content;
}

if (isset($_GET['url'])) {
    $file = $_GET['url'];
    echo readFileContent($file);
} else {
    echo "Supply a URL using the 'url' query parameter.";
}
?>
