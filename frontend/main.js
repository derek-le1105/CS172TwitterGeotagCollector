// Global Variables
var tweetIDs = [];
var tweets = [];
let searchString = "";
var timer;
const tweetContainer = document.getElementById('tweet-container');
const checkBox = document.getElementById("pauseBox");
const searchBar = document.getElementById("searchBar");
const url = "http://ec2-18-209-247-77.compute-1.amazonaws.com:3000/feed/random?q=weather"; // specify a url, in this case our web server


// Fetch first set of tweets
function getTweets() {
    fetch(url)
        .then(res => res.json())
        .then(data => {  
            for(let i=0; i < data.statuses.length; ++i) {
                tweets.push(data.statuses[i]);
            }

            refreshTweets();
        })
        .catch(err => {
            // error catching
            console.log(err);
        }) 
}


// Remove duplicates in tweets array
function removeDuplicates() {
    let i = 0;

    while (i < tweets.length) {
        if (!tweetIDs.includes(tweets[i].id)) {
            tweetIDs.push(tweets[i].id);
        }
        else {
            tweets.splice(i,1);
        }
        
        i++;
    }
}


// Listens to see if characters are added to search bar which then uses that to filter tweets
searchBar.addEventListener('input', (event) => {
    //searchString = event.target.value.trim().toLowerCase();
    searchString = searchBar.value;
    filteredResult = tweets.filter(tweet_list => tweet_list.text.search(searchString) != -1);

    while (tweetContainer.firstChild) {
        tweetContainer.removeChild(tweetContainer.firstChild);
    }

    filteredResult.forEach(tweetObject => {
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
});


// Initialize by getting first set of tweets
getTweets(); 
