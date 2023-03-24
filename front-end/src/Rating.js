import React from 'react';
import { Card, CardContent, Typography, Rating } from '@mui/material';

const RatingCard = ({ title, rating }) => {
  return (
    <Card>
      <CardContent>
        <Typography variant="h5" component="div">
          {title}
        </Typography>
        <Rating value={rating} precision={0.1} readOnly />
      </CardContent>
    </Card>
  );
};

export default RatingCard;