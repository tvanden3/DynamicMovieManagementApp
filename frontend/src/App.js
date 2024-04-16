import { TextField, List, ListItem, ListItemIcon, ListItemText } from '@mui/material';
import { useState, useEffect } from 'react';
import './App.css';
import LocalMoviesIcon from '@mui/icons-material/LocalMovies';

function App() {
  const [movieId, setMovieId] = useState("1"); 
  const [movie, setMovie] = useState(null); 

  useEffect(() => {
    if (movieId === "") {
      setMovie(null); 
    } else {
      fetch(`http://127.0.0.1:8000/movie/${movieId}`)
        .then(result => result.json()) 
        .then(result => {
          console.log(`Data received for movie ID ${movieId}:`, result);
          setMovie(result); 
        })
        .catch(error => {
          console.error('Error fetching movie:', error); 
        });
    }
    console.log('Current movieId:', movieId); 
  }, [movieId]); 

  useEffect(() => {
    console.log('Current movie:', movie);
  }, [movie]); 


  return (
    <div className="App">
      <header className="App-header">
        <TextField
          id="outlined-basic"
          label="Movie Id"
          variant="outlined"
          color="warning"
          focused
          value={movieId}
          onChange={e => setMovieId(e.target.value)} 
        />
        <List>
          {movie && (
            <ListItem>
              <ListItemIcon>
                <LocalMoviesIcon /> // Display a movie icon next to the movie name
              </ListItemIcon>
              <ListItemText primary={movie['name']} /> // Display the movie name
            </ListItem>
          )}
        </List>
      </header>
    </div>
  );
}

export default App; 
