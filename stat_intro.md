
![](images/stat_intro.pdf-0001-00.png)


# **STATISTICS** 

##### **Fourth Edition** 

**David Freeman, Robert Pisani, and Roger Purves** 

Statistics Fourth Edition 

### DAVID FREEDMAN ROBERT PISANI ROGER PURVES 

Statistics Fourth Edition 

W • W • NORTON & COMPANY 

NEW YORK • LONDON 


![](images/stat_intro.pdf-0005-04.png)


Copyright ⃝c 2007, 1998, 1991, 1978 by W. W. Norton & Company, Inc. All rights reserved. 

Printed in the United States of America. 

_Cartoons by Dana Fradon and Leo Cullum_ 

The text of this book is composed in Times Roman. Composition by Integre Technical Publishing Company, Inc. Manufacturing by R. R. Donnelley. 

###### **Library of Congress Cataloging-in-Publication Data** 

Freedman, David, 1938– 

Statistics. — 4th ed. / David Freedman, Robert Pisani, Roger Purves. 

p. cm. Rev. ed. of: Statistics / David Freedman _. . ._ [et al.], 3rd ed. ⃝c 1998. 

Includes bibliographical references and index. 

**ISBN 0-393-92972-8 ISBN 13-978-0-393-92972-0** 

1. Mathematical statistics. I. Pisani, Robert. II. Purves, Roger. III. Statistics. IV. Title. QA276.F683 519.5—dc21 

W.W. Norton & Company, Inc., 500 Fifth Avenue, New York, N.Y. 10110 http://www.wwnorton.com 

W.W. Norton & Company Ltd., Castle House, 75/76 Wells Street, London W1T 3QT 

1 2 3 4 5 6 7 8 9 0 

###### To Jerzy Neyman (1894–1981) 

_Born in Russia, Neyman worked in Poland and England before coming to the United States in 1938. He was one of the great statisticians of our time._ 

## Contents 

###### **Preface** 

###### **xv** 

###### **PART I. DESIGN OF EXPERIMENTS** 

**Chapter 1. Controlled Experiments 3** 

1. The Salk Vaccine Field Trial 3 2. The Portacaval Shunt 7 3. Historical Controls 8 4. Summary 10 

###### **Chapter 2. Observational Studies** 

**12** 

1. Introduction 12 2. The Clofibrate Trial 13 3. More Examples 15 4. Sex Bias in Graduate Admissions 17 5. Confounding 20 6. Review Exercises 24 7. Summary and Overview 27 

###### **PART II. DESCRIPTIVE STATISTICS** 

###### **Chapter 3. The Histogram** 

**31** 

1. Introduction 31 2. Drawing a Histogram 35 3. The Density Scale 38 4. Variables 42 

5. Controlling for a Variable 45 6. Cross-Tabulation 47 7. Selective Breeding 48 8. Review Exercises 50 9. Summary 56 

###### **Chapter 4. The Average and the Standard Deviation** 

**57** 

1. Introduction 57 2. The Average 58 

3. The Average and the Histogram 61 4. The Root-Mean-Square 66 5. The Standard Deviation 67 6. Computing the Standard Deviation 71 7. Using a Statistical Calculator 74 

8. Review Exercises 74 9. Summary 76 

viii CONTENTS 

**78** 

###### **Chapter 5. The Normal Approximation for Data** 

1. The Normal Curve 78 2. Finding Areas under the Normal Curve 82 3. The Normal Approximation for Data 85 4. Percentiles 88 5. Percentiles and the Normal Curve 90 6. Change of Scale 92 7. Review Exercises 93 8. Summary 96 

**Chapter 6. Measurement Error** 

**97** 

1. Introduction 97 2. Chance Error 97 3. Outliers 102 4. Bias 103 5. Review Exercises 104 6. Special Review Exercises 105 7. Summary and Overview 108 

**Chapter 7. Plotting Points and Lines** 

**Plotting Points and Lines 110** 1. Reading Points off a Graph 110 2. Plotting Points 112 3. Slope and Intercept 113 4. Plotting Lines 114 5. The Algebraic Equation for a Line 115 

###### **PART III. CORRELATION AND REGRESSION** 

**Chapter 8. Correlation** 

**119** 

1. The Scatter Diagram 119 2. The Correlation Coefficient 125 3. The SD Line 130 4. Computing the Correlation Coefficient 132 5. Review Exercises 134 6. Summary 139 

**Chapter 9. More about Correlation** 

**More about Correlation 141** 1. Features of the Correlation Coefficient 141 2. Changing SDs 144 3. Some Exceptional Cases 147 4. Ecological Correlations 148 5. Association is Not Causation 150 6. Review Exercises 153 7. Summary 157 

###### **Chapter 10. Regression** 

**158** 

1. Introduction 158 2. The Graph of Averages 162 

CONTENTS ix 

3. The Regression Method for Individuals 165 4. The Regression Fallacy 169 5. There Are Two Regression Lines 174 6. Review Exercises 176 7. Summary 178 

###### **Chapter 11. The R.M.S. Error for Regression** 

**180** 

1. Introduction 180 2. Computing the R.M.S. Error 185 3. Plotting the Residuals 187 4. Looking at Vertical Strips 190 5. Using the Normal Curve Inside a Vertical Strip 195 6. Review Exercises 198 7. Summary 201 

###### **Chapter 12. The Regression Line** 

**202** 

1. Slope and Intercept 202 2. The Method of Least Squares 208 3. Does the Regression Make Sense? 211 4. Review Exercises 213 5. Summary and Overview 216 

###### **PART IV. PROBABILITY** 

###### **Chapter 13. What Are the Chances?** 

**221** 

1. Introduction 221 2. Conditional Probabilities 226 3. The Multiplication Rule 228 4. Independence 230 5. The Collins Case 233 6. Review Exercises 234 7. Summary 236 

###### **Chapter 14. More about Chance** 

**237** 

1. Listing the Ways 237 2. The Addition Rule 241 3. Two FAQs (Frequently Asked Questions) 243 4. The Paradox of the Chevalier De M´er´e 248 5. Are Real Dice Fair? 252 6. Review Exercises 252 7. Summary 254 

###### **Chapter 15. The Binomial Formula** 

- **The Binomial Formula 255** 1. Introduction 255 2. The Binomial Formula 259 3. Review Exercises 261 4. Special Review Exercises 263 5. Summary and Overview 268 

CONTENTS 

x 

###### **PART V. CHANCE VARIABILITY** 

###### **Chapter 16. The Law of Averages** 

**The Law of Averages 273** 1. What Does the Law of Averages Say? 273 2. Chance Processes 278 3. The Sum of Draws 279 4. Making a Box Model 281 5. Review Exercises 285 6. Summary 287 **288** 

###### **Chapter 17. The Expected Value and Standard Error** 

1. The Expected Value 288 2. The Standard Error 290 3. Using the Normal Curve 294 4. A Short-Cut 298 5. Classifying and Counting 299 6. Review Exercises 304 7. Postscript 307 8. Summary 307 

**Chapter 18. The Normal Approximation for Probability Histograms** 

**308** 

1. Introduction 308 

2. Probability Histograms 310 3. Probability Histograms and the Normal Curve 315 4. The Normal Approximation 317 5. The Scope of the Normal Approximation 319 6. Conclusion 325 7. Review Exercises 327 8. Summary 329 

###### **PART VI. SAMPLING** 

###### **Chapter 19. Sample Surveys** 

- **Sample Surveys 333** 1. Introduction 333 2. The _Literary Digest_ Poll 334 3. The Year the Polls Elected Dewey 337 4. Using Chance in Survey Work 339 5. How Well Do Probability Methods Work? 342 6. A Closer Look at the Gallup Poll 343 7. Telephone Surveys 346 8. Chance Error and Bias 348 9. Review Exercises 351 10. Summary 353 

###### **Chapter 20. Chance Errors in Sampling** 

**355** 

1. Introduction 355 2. The Expected Value and Standard Error 359 3. Using the Normal Curve 362 

CONTENTS xi 

4. The Correction Factor 367 5. The Gallup Poll 370 6. Review Exercises 371 7. Summary 373 

###### **Chapter 21. The Accuracy of Percentages** 

**375** 

1. Introduction 375 2. Confidence Intervals 381 3. Interpreting a Confidence Interval 383 4. _Caveat Emptor_ 387 5. The Gallup Poll 389 6. Review Exercises 391 7. Summary 394 

###### **Chapter 22. Measuring Employment and Unemployment** 

- **Measuring Employment and Unemployment 395** 1. Introduction 395 2. The Design of the Current Population Survey 396 3. Carrying out the Survey 398 4. Weighting the Sample 401 5. Standard Errors 402 6. The Quality of the Data 404 7. Bias 404 8. Review Exercises 405 9. Summary 407 

###### **Chapter 23. The Accuracy of Averages** 

**409** 

1. Introduction 409 2. The Sample Average 415 3. Which SE? 422 4. A Reminder 424 5. Review Exercises 425 6. Special Review Exercises 428 7. Summary and Overview 436 

###### **PART VII. CHANCE MODELS** 

###### **Chapter 24. A Model for Measurement Error** 

- **A Model for Measurement Error 441** 1. Estimating the Accuracy of an Average 441 2. Chance Models 445 3. The Gauss Model 450 4. Conclusion 454 5. Review Exercises 455 6. Summary 457 

###### **Chapter 25. Chance Models in Genetics** 

- **Chance Models in Genetics 458** 1. How Mendel Discovered Genes 458 2. Did Mendel’s Facts Fit His Model? 463 3. The Law of Regression 465 

xii CONTENTS 

4. An Appreciation of the Model 468 5. Review Exercises 470 6. Summary and Overview 471 

###### **PART VIII. TESTS OF SIGNIFICANCE** 

###### **Chapter 26.** 

**475** 

1. Introduction 475 2. The Null and the Alternative 477 3. Test Statistics and Significance Levels 478 4. Making a Test of Significance 482 5. Zero-One Boxes 483 6. The _t_ -Test 488 7. Review Exercises 495 8. Summary 500 

**Chapter 27. More Tests for Averages** 

**501** 

1. The Standard Error for a Difference 501 2. Comparing Two Sample Averages 503 

3. Experiments 508 4. More on Experiments 512 5. When Does the _z_ -Test Apply? 517 6. Review Exercises 518 7. Summary 521 

**Chapter 28. The Chi-Square Test** 

**523** 

1. Introduction 523 2. The Structure of the _χ_<sup>2</sup> -Test 530 3. How Fisher Used the _χ_<sup>2</sup> -Test 533 4. Testing Independence 535 5. Review Exercises 540 6. Summary 544 **A Closer Look at Tests of Significance 545** 

###### **Chapter 29.** 

1. Was the Result Significant? 545 2. Data Snooping 547 3. Was the Result Important? 552 4. The Role of the Model 555 5. Does the Difference Prove the Point? 560 6. Conclusion 562 7. Review Exercises 563 8. Special Review Exercises 565 9. Summary and Overview 576 

|**Notes**|**A3**|
|---|---|
|**Answers to Exercises**|**A43**|
|**Tables**|**A104**|
|**Index**|**A107**|



## Preface 

_What song the Sirens sang, or what name Achilles assumed when he hid among women, though puzzling questions, are not beyond all conjecture._ 

—SIR THOMAS BROWNE (ENGLAND, 1605–1682) 

###### TO THE READER 

We are going to tell you about some interesting problems which have been studied with the help of statistical methods, and show you how to use these methods yourself. We will try to explain why the methods work, and what to watch out for when others use them. Mathematical notation only seems to confuse things for many people, so this book relies on words, charts, and tables; there are hardly any _x_ ’s or _y_ ’s. As a matter of fact, even when professional mathematicians read technical books, their eyes tend to skip over the equations. What they really want is a sympathetic friend who will explain the ideas and draw the pictures behind the equations. We will try to be that friend, for those who read our book. 

###### WHAT IS STATISTICS? 

Statistics is the art of making numerical conjectures about puzzling questions. 

- What are the effects of new medical treatments? 

- What causes the resemblance between parents and children, and how strong is that force? 

- Why does the casino make a profit at roulette? 

- Who is going to win the next election? by how much? 

- How many people are employed? unemployed? 

These are difficult issues, and statistical methods help a lot if you want to think about them. The methods were developed over several hundred years by people who were looking for answers to their questions. Some of these people will be introduced later. 

###### AN OUTLINE 

Part I is about designing experiments. With a good design, reliable conclusions can be drawn from the data. Some badly-designed studies are discussed too—so you can see the pitfalls, and learn what questions to ask when reading about a study. Study design is perhaps our most important topic; that is why we start there. The ideas look simple, but appearances may be deceptive: part I has a lot of depth. 

###### xiv PREFACE 

Studies typically produce so many numbers that summaries are needed. Descriptive statistics—the art of summarizing data—is introduced in part II. Histograms, the average, the standard deviation, and the normal curve are all considered. The discussion continues in part III, where the focus is on analyzing relationships, for instance, the dependence of income on education. Here, correlation and regression are the main topics. 

Much statistical reasoning depends on the theory of probability, discussed in part IV; the connection is through chance models, which are developed in part V. Coins, dice, and roulette wheels are the main examples in parts IV and V. The expected value and standard error are introduced; probability histograms are developed, and convergence to the normal curve is discussed. 

Statistical inference—making valid generalizations from samples—is the topic of parts VI–VIII. Part VI is about estimation. For instance, how does the Gallup Poll predict the vote? Why are some methods for drawing samples better than others? Part VII uses chance models to analyze measurement error, and to develop genetic theory. Part VIII introduces tests of significance, to judge whether samples are consistent with hypotheses about the population. As parts VI–VIII show, statistical inferences depend on chance models. If the model is wrong, the resulting inference may be quite shaky. 

Nowadays, inference is the branch of statistics most interesting to professionals. However, non-statisticians often find descriptive statistics a more useful branch, and the one that is easier to understand. That is why we take up descriptive statistics before inference. The bare bones of our subject are presented in chapters 1 to 6, 13, 16 to 21, 23, and 26. After that, the reader can browse anywhere. The next chapters to read might be 8, 10, 27, and 29. 

###### EXERCISES 

The sections in each chapter usually have a set of exercises, with answers at the back of the book. If you work these exercises as they come along and check the answers, you will get practice in your new skills—and find out the extent to which you have mastered them. Every chapter (except 1 and 7) ends with a set of review exercises. The book does not give answers for those exercises. Chapters 6, 15, 23, and 29 also have “special review exercises,” covering all previous material. Such exercises must be answered without the clues provided by context. 

When working exercises, you might be tempted to flip backward through the pages until the relevant formula materializes. However, reading the book backward will prove very frustrating. Review exercises demand much more than formulas. They call for rough guesses and qualitative judgments. In other words, they require a good intuitive understanding of what is going on. The way to develop that understanding is to read the book forward. 

Why does the book include so many exercises that cannot be solved by plugging into a formula? The reason is that few real-life statistical problems can be solved that way. Blindly plugging into statistical formulas has caused a lot of confusion. So this book teaches a different approach: thinking. 

PREFACE xv 

###### GRAPHICS 

As in previous editions, extensive use is made of computer graphics to display the data. Working drawings, however, are done freehand; the reader is encouraged to make similar sketches, rather than being intimidated by too much precision. The book still features cartoons by Dana Fradon of _The New Yorker_ . 

###### What’s New in the Fourth Edition? 

_Of the making of books, there is no end._ — _Ecclesiastes_ 

The principal change is to the data. Statistics, like people, show wear and tear from aging. Fortunately or unfortunately, data are easier to rejuvenate. We started the first edition in 1971, and completed the fourth in 2006. These past 35 years were years of rapid change, as commentators have doubtless observed since prehistoric times. 

There was explosive growth in computer use. Other technical developments include email _(_ + _)_ , the world wide web _(_ + _)_ , Windows _(_ ± _)_ , cell phones _(_ ± _)_ , and call centers with voice-activated menus _(_ − _)_ . SAT scores bottomed out around 1990, and have since been slowly going up (chapter 5). Educational levels have been steadily increasing (chapter 4), but reading skills may—or may not—be in decline (chapter 27). 

The population of the United States increased from 200 million to 300 million (chapter 24). There was corresponding growth in higher education. Over the period 1976 to 1999, the number of colleges and universities increased from about 3,000 to 4,000 (chapter 23). Student enrollments increased by about 40%, while the professoriate grew by 60%. The number of male faculty increased from 450,000 to 600,000; for women, the increase was 175,000 to 425,000. Student enrollments shifted from 53% male to 43% male. 

There were remarkable changes in student attitudes (chapters 27, 29). In 1970, 60% of first-year students thought that capital punishment should be abolished; by 2000, only 30% favored abolition. In 1970, 36% of them thought that “being very well off financially” was “very important or essential”; by 2000, the figure was 73%. 

The American public gained a fraction of an inch in height, and 20 pounds in weight (chapter 4). Despite the huge increase in obesity, there were steady gains in life expectancy—about 7 years over the 35-year period. Gain in life expectancy is a process (“the demographic transition”) that started in Europe around 1800. The trend toward longer lives has major societal implications, as well as ripple effects on our exercises. 

Family incomes went up by a factor of four, although much of the change represents a loss of purchasing power in the dollar (chapter 3). Crime rates peaked somewhere around 1990, and have fallen precipitously since (chapters 2, 29). Jury awards in civil cases once seemed out of control, but have declined since the 1990s 

xvi PREFACE 

along with crime rates. (See chapter 29; is this correlation or causation?) Our last topic is a perennial favorite: the weather. We have no significant changes to report (chapters 9, 24).<sup>∗</sup> 

###### ACKNOWLEDGMENTS FOR THE FOURTH EDITION 

Technical drawings are by Dale Johnson and Laura Southworth. Type was set in TEX by Integre. Nick Cox (Durham), Russ Lyons (Indiana), Josh Palmer (Berkeley), and Sam Rose (Berkeley) gave us detailed and useful feedback. M´aire N´ı Bhrolch´ain (Southampton), David Card (Berkeley), Rob Hollister (Swarthmore), Diana Petitti (Kaiser Permanente), and Philip Stark (Berkeley) helped us navigate the treacherous currents of the scholarly literature, and the even more treacherous currents of the world wide web. 

###### ACKNOWLEDGMENTS FOR PREVIOUS EDITIONS 

Helpful comments came from many sources. For the third edition, we thank Mike Anderson (Berkeley), Dick Berk (Pennsylvania), Jeff Fehmi (Arizona), David Kaye (Arizona), Steve Klein (Los Angeles), Russ Lyons (Indiana), Mike Ostland (Berkeley), Erol Pekoz (Boston), Diana Petitti (Kaiser Permanente), Juliet Shaffer (Berkeley), Bill Simpson (Winnipeg), Terry Speed (Berkeley), Philip Stark (Berkeley), and Allan Stewart-Oaten (Santa Barbara). Ani Adhikari (Berkeley) participated in the second edition, and had many good comments on the third edition. 

The writing of the first edition was supported by the Ford Foundation (1973– 1974) and by the Regents of the University of California (1974–75). Earl Cheit and Sanford Elberg (Berkeley) provided help and encouragement at critical times. Special thanks go to our editor, Donald Lamm, who somehow turned a permanently evolving manuscript into a book. Finally, we record our gratitude to our students, and other readers of our several editions and innumerable drafts. 


![](images/stat_intro.pdf-0018-07.png)


> ∗Most of the data cited here come from the _Statistical Abstract of the United States_ , various editions. See chapter notes for details. On trends in life expectancy, see Dudley Kirk, “Demographic transition theory,” _Population Studies_ vol. 50 (1996) pp. 361–87. 

#### PART I 

# Design of Experiments 

