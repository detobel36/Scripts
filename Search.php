<?php

function search($path) {
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
            $matches = array_merge($matches, search($search . "/*"));
            if($debug) {
                echo "<br /><br />";
            }
        } else {
            $contents = file_get_contents($search);
            if (!strpos($contents, "bdd.phoenix-rebirth.fr") != -1) {
                $matches[] = $search;
                if($debug) {
                    echo "TROUVE !!!<br /><br />";
                }
            }
        }

    }
    return $matches;
}

$matches = search("./*");

echo "<h3>Résultats:</h3>";
echo "<ul>";
foreach ($matches as $result) {
    echo "<li>".$result . "</li>";
}
echo "</ul>";

