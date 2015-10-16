import media

title = "Toy Story"
storyline = "A story of a boy and his toys that come to life"
poster_image_url = "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg"
trailer_youtube_url = "https://www.youtube.com/watch?v=vwyZH85NQC4"

toy_story = media.Movie(title, storyline, poster_image_url, trailer_youtube_url)

print(toy_story.storyline)
