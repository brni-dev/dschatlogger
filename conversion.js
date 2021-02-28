function findMention(text) {
    var start = false;
    var mention = '';

    for (var i = 0; i < text.length; i ++) {
        if (text.charAt(i) == '<' && text.charAt(i + 1) == '@') start = true;
        if (start == true) mention += text.charAt(i);
        if (text.charAt(i) == '>') start = false;
    };
    return mention;
};

function convertMention(text) {
    var id = '';
    for (var i = 3; i < text.length - 1; i ++) {
        id += text.charAt(i);
    };

    return id;
};