from ..wordcloud.wordcloud import WordCloud

wc = WordCloud(
                background_color='white',
                width=800,
                height=600,
                contour_width=5,
                prefer_horizontal=1,
                max_words = 100,
                collocations = True,
                contour_color='steelblue',
                min_font_size = 15,
                random_state=21
                )
wc.generate("The cat chased the cat through the yard while the dog watched. She loves to read books, especially mystery books and fantasy books. The sunset was so beautiful that everyone stopped to admire the beautiful view. He always chooses chocolate ice cream because chocolate is his favorite flavor. In the garden, the roses bloomed, and the roses filled the air with a sweet fragrance.")

