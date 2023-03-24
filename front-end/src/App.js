import React, { useState } from 'react';
import './App.css';
import {Container, TextField, Button, Box, Grid} from '@mui/material';
import axios from 'axios';
import RatingCard from "./Rating";
import CircularRating from "./CircularRating";
import Rating from '@mui/lab/Rating';


const App = () => {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/classify', { text });
      setResult(response.data);
    } catch (error) {
      console.error('Error fetching data', error);
    }
  };

  const ratings = [
    { title: 'Product A', rating: {result} },
  ];

  return (
    <Container>
      <h1>Text Processing</h1>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Text"
          multiline
          rows={4}
          fullWidth
          value={text}
          onChange={(event) => setText(event.target.value)}
        />
        <Box mt={2}>
          <Button type="submit" variant="contained" color="primary">
            Process Text
          </Button>
        </Box>
      </form>
      {"\n"}
      {result !== null && (

        <div className={"centered-div"}>
          <h2>Classification Result:</h2>
          {/*<CircularRating value={result.overall} maxValue={5} />*/}
          <Rating value={result.overall} max={5} precision={0.5} />
          <br />
          <CircularRating value={result.food} maxValue={5} />
          <CircularRating value={result.service} maxValue={5} />
          <br />
          <CircularRating value={result.ambience} maxValue={5} />
          <CircularRating value={result.anecdotes} maxValue={5} />
        </div>

      )}
    </Container>
  );
};

export default App;