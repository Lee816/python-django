function dark_or_light(self){
    var body = document.querySelector('body');
    var btn = document.querySelector('#changebtn');

    if (self.value == 'light'){
        body.style.backgroundColor = 'black';
        body.style.color = 'white';
        self.value = 'dark';
    } else{
        body.style.backgroundColor = 'white';
        body.style.color = 'black';
        self.value = 'light';
    }
}