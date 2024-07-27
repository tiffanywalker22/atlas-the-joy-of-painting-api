CREATE DATABASE joy_of_painting;

CREATE TABLE episodes (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    date DATE NOT NULL,
    month VARCHAR(50) NOT NULL,
    episode VARCHAR(20) NOT NULL,
    painting_index INT NOT NULL,
    img_src VARCHAR(255),
    youtube_src VARCHAR(255),
    num_colors INT NOT NULL,
    colors TEXT,
    subject TEXT,
    color_hex TEXT
);