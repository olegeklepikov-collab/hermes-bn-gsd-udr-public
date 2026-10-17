args <- commandArgs(trailingOnly=TRUE)
root <- args[[1]]
old <- args[[2]]
new <- args[[3]]
change <- function(x) {
 if (is.character(x)) return(gsub(old,new,x,fixed=TRUE))
 if (is.list(x)) {
  y <- lapply(unclass(x),change)
  attributes(y) <- attributes(x)
  return(y)
 }
 x
}
paths <- list.files(root,pattern="\\.rds$",recursive=TRUE,full.names=TRUE)
changed <- 0L
for (p in paths) {
 x <- readRDS(p); y <- change(x)
 if (!identical(x,y)) {saveRDS(y,p); changed <- changed+1L}
}
cat("R metadata files updated:",changed,"\n")
