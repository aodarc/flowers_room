let radio_answers = $('input[name="answer"]');
let question_title = $('#question-name');

function get_next_question(next_url) {
    if (next_url) {
        $.ajax({
            url: next_url
        }).done(function (data) {
            console.log("Sample of data:", data);

            question_title.text(data.results[0].title);

            if(data.next){
                // save next question in data attr
                question_title.data('next-question-id', data.next);
            }

            // deselect input when question was changed
            radio_answers.prop('checked', false);
        }).error(function (data) {
            console.log(data);
        });
    }
}


// event to change answer and get next question
radio_answers.on('change', function (event) {
    console.log('CHANGED ANSWER');

    // get next question
    const next_question_url = question_title.data('next-question-id');
    if(next_question_url){
        get_next_question(next_question_url)
    }
    else {
        console.log('This is the end');
    }
});