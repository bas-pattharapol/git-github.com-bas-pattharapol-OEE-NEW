<?php
error_reporting(E_ALL & ~E_NOTICE);



if (isset($_REQUEST["submit"])) {

    $allowedExts = array("jpg", "jpeg", "gif", "png");
    echo $_FILES["file"]["name"] . "     " . $_FILES["file"]["type"];

    $extension = end(explode(".", $_FILES["file"]["name"]));
      if ($_FILES["file"]["type"] == "image/jpeg" && $_FILES["file"]["size"] < 2500000 && in_array($extension, $allowedExts)) {
   //  if ($_FILES["file"]["type"] == "image/gif" || $_FILES["file"]["type"] == "image/jpg" || $_FILES["file"]["type"] == "image/jpeg" || $_FILES["file"]["type"] == "image/png" && $_FILES["file"]["size"] < 2500000 && in_array($extension, $allowedExts)) {

      if ($_FILES["file"]["error"] > 0) {

        echo "Error: " . $_FILES["file"]["error"] . "<br />";

      }
      else {

        # $fname = $_FILES["file"]["name"];
        # $fname = "datadisplay.jpg";
        $fname = $_FILES["file"]["name"];
        $uploadFileDir = '/var/www/html/neo/dist/img/';
        $dest_path = $uploadFileDir . $fname;
        move_uploaded_file($_FILES["file"]["tmp_name"], $dest_path);
	# copy($_FILES["file"]["tmp_name"], $fname);
        # echo "<br>Temp_Name: " . $_FILES["file"]["tmp_name"] . "<br>";

    # echo "ini:  " . ini_get('upload_tmp_dir') . "\n<br>";
    # echo "env:  " . sys_get_temp_dir()        . "\n<br>";
    # echo "temp: " . getenv('temp')            . "\n<br>";
    # echo "tmp:  " . getenv('tmp')             . "\n<br>";


        echo "Upload: " . $_FILES["file"]["name"] . "<br />";
        echo "Type: " . $_FILES["file"]["type"] . "<br />";
        echo "Size: " . ($_FILES["file"]["size"] / 1024) . " Kb<br />";
        echo "Stored in: " . $fname;

      }

    }
    else {

      echo "Invalid file type";

    }

}
?>
<form action="" method="post" enctype="multipart/form-data">
<input type="file" name="file" />
<input type="submit" name="submit" value="submit" />
</form>
