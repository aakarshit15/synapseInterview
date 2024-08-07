import bodyParser from "body-parser";
import express from "express";
import Book from "./BookModel.js";
import mongoose from "mongoose";
import env from "dotenv";

const app = express();
const port = 3000;
env.config();

const db = mongoose.connect(process.env.MONGO_LINK);

app.use(bodyParser.urlencoded({extended: true}));

app.get("/allBooks", async (req, res) => {
    try {
        let books = await Book.find();
        for (const [key, value] of Object.entries(req.query)) {
            books = books.filter((book) => {
                return `${book[key]}` == value;
            })
        }
        res.json({reqSuccess: true, allBooks: books});
    } catch (error) {
        console.log(`Error getting all books: ${error}`);
        res.json({reqSuccess: false, reqErrMsg: error});
    }
});

app.post("/createBook", async (req, res) => {
    try {
        const newBook = new Book(req.body);
        await newBook.save();
        res.json({reqSuccess: true});
    } catch (error) {
        console.error(`Error creating new book: ${error}`);
        res.json({reqSuccess: false, reqErrMsg: error});
    }
});

app.patch("/updateBook/:id", async (req, res) => {
    try {
        await Book.updateOne({_id: req.params.id}, req.body);
        res.status(201).json({reqSuccess: true});
    } catch(error) {
        console.error(`Error updating book: ${error}`);
        res.status(500).json({reqSuccess: false, reqErrMsg: error});
    }
});

app.delete("/deleteBook/:id", async (req, res) => {
    try {
        const book = await Book.findOneAndDelete({_id: req.params.id});
        res.status(200).json({reqSuccess: true, book: book});
    } catch (error) {
        console.error(`Error deleting book: ${error}`);
        res.status(500).json({reqSuccess: false, reqErrMsg: error});
    }
});

app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
});

