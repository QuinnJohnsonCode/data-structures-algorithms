import { revalidatePath } from "next/cache";
import { Post } from "./models";
import { connectToDb } from "./utils";

export const addPost = async (formData) => {
    "use server"

    // const title = formData.get("title");
    // const desc = formData.get("desc");
    // const slug = formData.get("slug");
    // //const userId = formData.get("userId");

    const { title, desc, slug, userId } = Object.fromEntries(formData);

    try {
        connectToDb();
        const newPost = new Post({
            title, 
            desc,
            slug,
            userId
        });
        
        await newPost.save();
        console.log("Saved to db.");
        revalidatePath("/blog"); // Will recache posts at /blog
    } catch (err) {
        console.log(err);
        throw new Error("Something went wrong...");
    }
    
};

export const deletePost = async (formData) => {
    "use server"

    // const title = formData.get("title");
    // const desc = formData.get("desc");
    // const slug = formData.get("slug");
    // //const userId = formData.get("userId");

    const { postId } = Object.fromEntries(formData);

    try {
        connectToDb();
        
        await Post.findByIdAndDelete({_id: postId});
        console.log("Deleted from db.");
        revalidatePath("/blog"); // Will recache posts at /blog
    } catch (err) {
        console.log(err);
        throw new Error("Something went wrong...");
    }
    
};