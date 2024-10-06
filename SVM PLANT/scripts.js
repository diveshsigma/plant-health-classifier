function previewImage() {
    const fileInput = document.getElementById('fileInput');
    const preview = document.getElementById('imagePreview');
    const file = fileInput.files[0];
    const reader = new FileReader();
    reader.addEventListener("load", function() {
        preview.src = reader.result;
        preview.style.display = 'block';
    }, false);
    if (file) {
        reader.readAsDataURL(file);
    }
}
function classifyPlant(event) {
    event.preventDefault(); 
    const results = ['Healthy', 'Not Healthy'];
    const randomResult = results[Math.floor(Math.random() * results.length)]; 
    const previewImageUrl = document.getElementById('imagePreview').src;
    displayResult(randomResult, previewImageUrl);
}
function displayResult(resultText, imageUrl) {
    const resultSection = document.getElementById('result');
    const classificationResult = document.getElementById('classificationResult');
    const uploadedImage = document.getElementById('uploadedImage');
    classificationResult.textContent = resultText;
    uploadedImage.src = imageUrl;
    if (resultText === 'Healthy') {
        classificationResult.style.color = 'green';
    } else {
        classificationResult.style.color = 'red';
    }
    resultSection.style.display = 'block';
}
