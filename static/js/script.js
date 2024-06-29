document.getElementById("submit").addEventListener("click", async () => {
    let trackingNumber = document.getElementById("main-tracker").value

    const regex = /^[RCEV][A-Z]\d{9}/gm
    const found = trackingNumber.match(regex)

    if (found) {
        const trackingInfo = await getTrackingInfo(trackingNumber)

        if (trackingInfo.status == "no_data" || trackingInfo.status == "wrong_code") {
            alert("Error")
            return
        }
    } else {
        alert("Error")
        return
    }
})

async function getTrackingInfo(trackingNumber) {
    try {
        const response = await fetch(`https://bgpost.dakovdev.com/api/v1/tracking?code=${trackingNumber}`)
        if (!response.ok) {
            throw new Error(response.statusText)
        }

        const trackingInfo = JSON.parse(response.json())

        return trackingInfo
    } catch (error) {
        alert(error)
    }
}