<?php

function search($path, $searchWord) {
    $debug = FALSE;
    $matches = array();
    foreach (glob($path) as $search) {
        if($debug) {
            echo "Recherche dans: " . $search . "<br />";
        }
        if(is_dir($search)) {
            if($debug) {
                echo "<br />Dossier: " . $search . "<br />";
            }
            $matches = array_merge($matches, search($search . "/*", $searchWord));
            if($debug) {
                echo "<br /><br />";
            }
        } else {
            $contents = file_get_contents($search);
            if (!strpos($contents, $searchWord) != -1) {
                $matches[] = $search;
                if($debug) {
                    echo "TROUVE !!!<br /><br />";
                }
            }
        }

    }
    return $matches;
}

$matches = search("./*", "exemple");

echo "<h3>Résultats:</h3>";
echo "<ul>";
foreach ($matches as $result) {
    echo "<li>".$result . "</li>";
}
echo "</ul>";

