document.addEventListener('DOMContentLoaded', function () {
    var img = document.createElement('img');
    document.getElementById('plot-container').appendChild(img);
    console.log(`running plot script`);

    setInterval(refreshPlot, 5000);

    function refreshPlot() {
        img.src = 'http://127.0.0.1:5501/plot';
        img.alt = "Temperature and Humidity Plot";
    
        // Append the image to the plotContainer div
        
    }
});