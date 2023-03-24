import React from 'react';
import { CircularProgress, Typography, Box } from '@mui/material';

const CircularRating = ({ value, maxValue = 5 }) => {
  const normalizedValue = (value / maxValue) * 100;

  return (
    <Box position="relative" display="inline-flex">
      <CircularProgress variant="determinate" value={normalizedValue} />
      <Box
        top={0}
        left={0}
        bottom={0}
        right={0}
        position="absolute"
        display="flex"
        alignItems="center"
        justifyContent="center"
      >
        <Typography variant="caption" component="div" color="text.secondary">
          {`${Math.round(value)} / ${maxValue}`}
        </Typography>
      </Box>
    </Box>
  );
};

export default CircularRating;