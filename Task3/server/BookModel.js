import mongoose from "mongoose";

const bookSchema = new mongoose.Schema({
    name: String,
    genre: String,
    author: String,
    inStock: Number,
    ratings: {
        type: Number,
        min: 1,
        max: 5
    }
});

const Book = mongoose.model("Book", bookSchema);

export default Book;

/*

Book Schema ------------------------------------->

{
    _id: ObjectId
    name: String
    genre: [String]
    author: String
    inStock: Number
    ratings: {
        type: Number,
        min: 1,
        max: 5
    }
}

*/