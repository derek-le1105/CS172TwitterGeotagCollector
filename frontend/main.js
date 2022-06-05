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
        for(let i=0; i < data.statuses.length; ++i) {
            tweets.push(data.statuses[i]);
        }

        showTweetsTweets();
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

    tweets.forEach(tweetObject => {
        // e.g. create a div holding tweet content
        const singleTweetContainer = document.createElement("div");
        singleTweetContainer.classList.add("tweets");

        let tweetProfilePic = document.createElement('img');
        tweetProfilePic.src = tweetObject.user.profile_image_url;
        tweetProfilePic.classList.add("tweet-picture-class");

        let tweetName = document.createElement("b");
        tweetName.textContent = tweetObject.user.name;
        tweetName.classList.add("tweet-name-class");

        let tweetUserName = document.createElement("b");
        tweetUserName.textContent = " @" + tweetObject.user.screen_name;
        tweetUserName.classList.add("tweet-username-class");

        let tweetDate = document.createElement("b");
        tweetDate.textContent = " " + tweetObject.user.created_at;
        tweetDate.classList.add("tweet-username-class");

        let tweetText = document.createElement("p");
        tweetText.textContent = tweetObject.text;

        // append the text node to the div
        singleTweetContainer.appendChild(tweetProfilePic);
        singleTweetContainer.appendChild(tweetName);
        singleTweetContainer.appendChild(tweetUserName);
        singleTweetContainer.appendChild(tweetDate);
        singleTweetContainer.appendChild(tweetText);

        // finally append your tweet into the tweet list
        tweetContainer.appendChild(singleTweetContainer);
    });
}