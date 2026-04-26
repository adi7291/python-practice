let sec = 3665;

let timer = setInterval(() => {
  if (sec < 0) {
    clearInterval(timer);
    console.log("times Up!!");
  } else {
    sec--;
    let seconds = sec % 60;
    let minutes = Math.floor((sec / 60) % 60);
    let hours = Math.floor(sec / 3600);
    console.log(
      `${hours.toString().padStart(2, "0")}:${minutes
        .toString()
        .padStart(2, "0")}:${seconds.toString().padStart(2, "0")}`
    );
  }
}, 1000);
