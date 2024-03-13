const fileInput = document.querySelector("#excel_file");
const fileInputLabel = document.querySelector("#label_for_input");

const submitBtn = document.querySelector("#label_for_submit");

const fileInputSuccessIcon = document.createElement('i')
fileInputSuccessIcon.classList.add('fa-solid', 'fa-circle-check')
fileInputSuccessIcon.id = "fileInputSuccessIcon"

fileInput.addEventListener('change', () => {
    if (fileInput.files.length > 0) {
        submitBtn.style.display = "flex"
        fileInputLabel.prepend(fileInputSuccessIcon)
    }
    else
        submitBtn.style.display = "none"

})