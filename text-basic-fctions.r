# Reads txt file from the connection; default UTF-8 encoding
## Output: raw txt file content
readMyTextFile   <- function(path) {
  myFile <- readChar(path, file.info(path)$size, useBytes = FALSE)

  return(myFile)
}

# Splitter/tokenizer – splits text according to a given regex
## Input: raw text; Output: tokens
tokenizeMyText  <-  function(text, 
                             regex = "[^\\p{L}\\p{N}]+", 
                             makeLower = FALSE) {
  require(stringr)
  tokens   <- unlist(str_split(text, 
                               regex, 
                               simplify = FALSE))
  tokens   <- tokens[tokens != ""]

  if (makeLower) {
    tokens  <-  tolower(tokens)
  }

  return(tokens)
}

# Dataframer – takes a list of values and returns a freq. data frame
## Input: list of values; Output: freq data frame
getFreqDF        <-  function(data) {
  freqDataFrame  <-  data.frame(sort(table(data),
                                decreasing = TRUE),
                                stringsAsFactors = FALSE)

  return(freqDataFrame)
}

# Words-of-frequency finder – retrieves words of a given (n)
# max freq from a data frame
## Input: data frame; Output: words of given frequency (vector)
getWordsWithNFreq <-  function(df, freqColName = "Freq",
                                   wordsColName = "data",
                                   n = 1) {
  if(ncol(df) >= 2){
    wordsWithNFreq  <-  df[which(df[, freqColName] <= n), wordsColName]
    return(as.character(wordsWithNFreq))
  }

  wordsWithNFreq  <-  rownames(df[which(df[, 1] <= n), ])
  return(as.character(wordsWithNFreq))
}

# Splitter – splits tokens into a given number of groups
## Input: (reduced) tokens; Output: list of groups
splitTokens <-  function(reducedTokens, nOfGroups = 2) {
  groups    <-  list()
  nOfGroupMembers  <- floor(length(reducedTokens) / nOfGroups)

  from  <- 1
  to    <-  nOfGroupMembers
  for (i in 1:nOfGroups) {
    currentGroup  <-  reducedTokens[from:to]
    groups[[i]]   <-  currentGroup

    from  <-  sum(lengths(groups)) + 1
    to    <-  from + nOfGroupMembers - 1
  }

  return(groups)
}

