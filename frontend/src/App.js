//import logo from './logo.svg';
import { TextField, List, ListItem, ListItemIcon, ListItemText} from '@mui/material';
import {useEffect, useState} from 'react';
import './App.css';
//import {Movie} from '@mui/icons-material';
import LocalMoviesIcon from '@mui/icons-material/LocalMovies'



function App() {
  const [movieId, setMovieId] = useState("1")
  const [movie, setMovie] = useState(null)

  useEffect(() => {
    if(movieId == ""){
      setMovie(null);
    }
    else{
      fetch(`http://127.0.0.1:8000/movie/${movieId}`)
      .then( result => result.json())
      .then( result => {
        console.log(`http://127.0.0.1:8000/movie/${movieId}`)
        setMovie(result)
            });
    }
    console.log(movieId);
  }, [movieId] );

  useEffect(() => {
    console.log(movie);
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
                <LocalMoviesIcon />
              </ListItemIcon>
              <ListItemText primary={movie['name']} />
            </ListItem>
          )}
        </List>
      </header>
    </div>
  );
}

export default App;
