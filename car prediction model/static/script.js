function predictPrice() {

    let data = {
        year: document.getElementById("year").value,
        present_price: document.getElementById("present_price").value,
        kms_driven: document.getElementById("kms_driven").value,
        fuel_type: document.getElementById("fuel_type").value,
        seller_type: document.getElementById("seller_type").value,
        transmission: document.getElementById("transmission").value,
        owner: document.getElementById("owner").value
    };

    fetch("/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(res => {
        document.getElementById("result").innerText = 
            "Predicted Price: ₹ " + res.price + " Lakhs";
    });
}
