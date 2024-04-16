//import logo from './logo.svg';
import { TextField, List, ListItem, ListItemIcon, ListItemText} from '@mui/material';
import {useState} from 'react';
import './App.css';

function App() {
  const [movieId, setMovieId] = useState("5")
  return (
    <div className="App">
      <header className="App-header">
        <TextField id="outlined-basic" label="Movie Id"
        variant ="outlined" color="warning" focuse value={movieId}
        onChange={e=> setMovieId(e.target.value)}
        />
      </header>
    </div>
  );
}

export default App;
