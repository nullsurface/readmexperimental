
// Trying to figure out how to 'insert' squares into canvas div
const gridContainer = $("#grid-container")

function sequenceStart() {
    for (i = 0; i < 7; i++) {
        for(j = 0; j < 48; j++){
            commitSquare = document.createElement('div');
            commitSquare.classList.add('commitSquare');
            gridContainer.appendChild(commitSquare.addClass('grid-container'));
        }
    }
}


sequenceStart();

