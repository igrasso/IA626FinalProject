library(readr)
library(ggplot2)
library(tidyverse)
library(chisq.posthoc.test)

# Read data, rename columns, order the data to be combined
census_race <- read_csv("../Data/census_race.csv", col_names = FALSE)
names(census_race) <- c("RACE", "POP")
census_race <- census_race[order(census_race$RACE),]
census_race <- census_race %>%
  mutate(PERCPOP = POP/sum(POP))

census_lang <- read_csv("../Data/census_language.csv", col_names = FALSE)
names(census_lang) <- c("LANG", "PERCPOP")
census_lang <- census_lang[order(census_lang$LANG),]

snap_race <- read_csv("../Data/snap_race.csv", col_names = FALSE)
names(snap_race) <- c("RACE", "POP")
snap_race <- snap_race[order(snap_race$RACE),]
snap_race <- snap_race %>% 
  mutate(PERCPOP = POP/sum(POP))

snap_lang <- read_csv("../Data/snap_language.csv", col_names = FALSE)
names(snap_lang) <- c("LANG", "POP" )
snap_lang <- snap_lang[order(snap_lang$LANG),]
snap_lang <- snap_lang %>%
  mutate(PERCPOP = POP/sum(POP)*100)

# Combine data to show proportionate representation
df_lrep <- data.frame(
  snap_percpop = snap_lang$PERCPOP/census_lang$PERCPOP,
  lang = snap_lang$LANG
)

df_rrep <- data.frame(
  snap_percpop = snap_race$PERCPOP/census_race$PERCPOP,
  race = snap_race$RACE
)

# Visualize language by representation
ggplot(df_lrep, aes(x = lang, y = snap_percpop)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_hline(yintercept = 1) +
  labs(
    title = "Representation by Language",
    x = "Primary Language",
    y = ""
  ) +
  coord_flip() +
  scale_y_continuous(breaks = c(seq(0, 1.2, 0.25)),
                     limits = c(0, 1.5),
                     labels = scales::percent) +
  scale_x_discrete(labels = c("English", "Other", "Spanish"), drop = FALSE) +
  geom_text(aes(label= paste0(round(snap_percpop*100, digits = 2), "%")),
            hjust=-.5, color="black", size=3, fontface = "bold") +
  theme_minimal() +
  theme(
    text = element_text(family = 'Gill Sans'),
    axis.text.x = element_blank()
  ) 

# Visualize race by representation
ggplot(df_rrep, aes(x = race, y = snap_percpop)) +
  geom_bar(stat = "identity", position = "dodge") +
  geom_hline(yintercept = 1) +
  labs(
    title = "Representation by Race",
    x = "Race",
    y = ""
  ) +
  coord_flip() +
  scale_y_continuous(breaks = c(seq(0, 35, 5)),
                     limits = c(0, 35),
                     labels = scales::percent) +
  geom_text(aes(label= paste0(round(snap_percpop*100, digits = 2), "%")),
            hjust=-.8, color="black", size=3, fontface = "bold") +
  theme_minimal() +
  theme(
    text = element_text(family = 'Gill Sans'),
    axis.text.x = element_blank()
  ) 

# Chi Squared goodness of fit tests
chisq.test(snap_race$POP, p = census_race$PERCPOP)
chisq.test(snap_lang$POP, p = census_lang$PERCPOP/100)

# Create tables for post hoc analysis
t = as.table(as.matrix(data.frame(n = snap_race$POP, p = census_race$PERCPOP)))
dimnames(t) <- list(race = c("Asian", "Black/African American",
                             "Native American/Alaskan Native",
                             "Native Hawaiian/Pacific Islander",
                             "Other", "White"),
                    dataset = c("SNAP", "Census"))


t2 = t = as.table(as.matrix(data.frame(n = snap_lang$POP, p = census_lang$PERCPOP)))
dimnames(t2) <- list(
  language = c("English", "Other", "Spanish"),
  dataset = c("SNAP", "Census")
)

# Post hoc analysis for race and primary language spoken respectively
chisq.posthoc.test(x = t, method = "bonferroni")
chisq.posthoc.test(x = t2, method = "bonferroni")
