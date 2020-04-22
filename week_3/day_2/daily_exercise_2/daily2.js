let libButton = document.getElementById('lib-button');
    let libIt = function() {
        let storyDiv = document.getElementById("story");
        storyDiv.innerHTML = "??Your story here";
    };
    libButton.addEventListener('click', libIt);
