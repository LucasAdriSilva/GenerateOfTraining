var progressBar = document.getElementById('progress-bar');
var timer;
var duration = 180; // Duração em segundos (3 minutos)
var remainingTime = duration;
var currentProgress = 0;

export function creatCronometro() {
    document.getElementById('accountant').innerHTML != `` ? stopCounter() : null
    
    document.getElementById('accountant').classList.remove('d-none')

    const accountant = document.getElementById('accountant')
    accountant.innerHTML = ` 
    <div class="row pe-3 ps-3 pt-2 pb-2 reset-Padding">

        <div class="col-2 d-flex justify-content-center align-items-center">
            <svg id="cronometroIcon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="#545454" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-clock"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
        </div>

        <div class="col-7 ">
            <div class="w-100 d-flex justify-content-center align-items-center gap-2">
                <button onclick="decrementDuration()" class="btn-escrito">-10s</button>
                <span id="cronometro">03:00</span>
                <button onclick="incrementDuration()" class="btn-escrito">+10s</button>
            </div>

            <div class="progress mt-1" role="progressbar" aria-label="Animated striped example" aria-valuenow="100"
                aria-valuemin="0" aria-valuemax="100">
                <div id="progress-bar" class="progress-bar progress-bar-striped progress-bar-animated"
                    style="width: 100%"></div>
            </div>

        </div>

        <div class="col-3 d-flex justify-content-center align-items-center">
            <button class="btn-stoped" onclick="stopCounter()">Pular</button>
        </div>
    </div>
`


    function updateProgress() {
        progressBar = document.getElementById('progress-bar');
        remainingTime--;
        currentProgress = (remainingTime / duration) * 100;
        progressBar.style.width = currentProgress + '%';

        var minutes = Math.floor(remainingTime / 60);
        var seconds = remainingTime % 60;

        var displayMinutes = minutes < 10 ? '0' + minutes : minutes;
        var displaySeconds = seconds < 10 ? '0' + seconds : seconds;

        document.getElementById('cronometro').innerText = displayMinutes + ':' + displaySeconds;

        if (remainingTime <= 0) {
            stopCounter()
            
        }
    }

    function startCounter() {
        timer = setInterval(updateProgress, 1000);
    }
    startCounter()
}

export function stopCounter() {
    clearInterval(timer);
    duration = 180;
    remainingTime = duration
    currentProgress = 0
    document.getElementById('accountant').innerHTML = ``
    document.getElementById('accountant').classList.add('d-none')

}

export function incrementDuration() {
    var timeToAdd = 10;
    duration += timeToAdd;
    remainingTime += timeToAdd;
    currentProgress = (remainingTime / duration) * 100;
    progressBar.style.width = currentProgress + '%';
}

export function decrementDuration() {
    var timeToSubtract = 10;
    if (duration > timeToSubtract) {
        duration -= timeToSubtract;
        remainingTime = Math.max(remainingTime - timeToSubtract, 0);
        currentProgress = (remainingTime / duration) * 100;
        progressBar.style.width = currentProgress + '%';
    }
}



