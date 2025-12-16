// Show image preview
function previewImage() {
    const fileInput = document.getElementById("fileInput");
    const previewImg = document.getElementById("previewImg");

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        previewImg.src = URL.createObjectURL(file);
        previewImg.style.display = "block";
    }
}

async function uploadImage() {

    const fileInput = document.getElementById("fileInput");
    const resultDiv = document.getElementById("result");

    if (fileInput.files.length === 0) {
        alert("Please select an image first");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    resultDiv.innerHTML = "<p>Predicting...</p>";

    try {
        const response = await fetch("/predict", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        const badgeClass = data.prediction === "OPEN"
            ? "badge-open"
            : "badge-close";

        resultDiv.innerHTML = `
            <p>Status:</p>
            <span class="${badgeClass}">
                ${data.prediction}
            </span>
            <p>Confidence: ${(data.confidence * 100).toFixed(2)}%</p>
        `;

    } catch (error) {
        console.error(error);
        resultDiv.innerHTML = "<p>Error occurred. Try again.</p>";
    }
}
