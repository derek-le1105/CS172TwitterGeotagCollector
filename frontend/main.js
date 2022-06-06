// Global Variables
var tweets = [];
const tweetContainer = document.getElementById('tweet-container');
const searchBar = document.getElementById("searchBar");
const url = "http://127.0.0.1:5000/getData"; // specify a url, in this case our web server

// Fetch first set of tweets
function getTweets() {
    fetch(url, {
        method: 'POST',
        mode: 'cors', // this cannot be 'no-cors'
        headers: {'Content-Type': 'application/json'}, //NOT SURE ABOUT THIS PART
        body: JSON.stringify({
            dataToFetch: searchBar.value
        })
    })
    .then(res => res.json())
    .then(data => {
        console.log(data);
        tweets = []
        for(let i=0; i < data.hits.hits.length; ++i) {
            tweets.push(data.hits.hits[i]);
        }

        showTweets();
    })
    .catch(err => {
        // error catching
        console.log(err);
    }) 
}

// Show tweets that were queried
function showTweets() {
    while (tweetContainer.firstChild) {
        tweetContainer.removeChild(tweetContainer.firstChild);
    }

    console.log(tweets)
    tweets.forEach(tweetObject => {
        // e.g. create a div holding tweet content
        const singleTweetContainer = document.createElement("div");
        singleTweetContainer.classList.add("tweets");

        let tweetDate = document.createElement("b");
        tweetDate.textContent = tweetObject._source.created_at;
        tweetDate.classList.add("tweet-username-class");

        let tweetText = document.createElement("p");
        tweetText.textContent = tweetObject._source.text;

        // append the text node to the div
        singleTweetContainer.appendChild(tweetDate);
        singleTweetContainer.appendChild(tweetText);

        // finally append your tweet into the tweet list
        tweetContainer.appendChild(singleTweetContainer);
    });
}