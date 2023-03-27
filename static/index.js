function generateStars(rating) {
    if (rating === null){
        console.log(rating)
        return "Not enough ratings for the Selected Category"
    }
    else {
        console.log(rating)
        const filledStars = '★'.repeat(Math.round(rating));
        const emptyStars = '☆'.repeat(5 - Math.round(rating));
        return filledStars + emptyStars;
    }
}

const starContainers = document.querySelectorAll('.stars');
starContainers.forEach(container => {
    const rating = container.getAttribute('data-rating');
    container.innerHTML = generateStars(rating);
});