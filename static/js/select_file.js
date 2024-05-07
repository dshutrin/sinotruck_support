function set_file_name() {
    let file_input = document.getElementById("id_document");
    let filename = file_input.files[0].name
    document.getElementById("choice_file").innerText = filename;
}
