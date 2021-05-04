bedahdata=as.data.frame(bedah_data)
bedahdata %>% count()
setwd("/Users/hendrasetiawan/Documents/2021 Case Competition Participant Data")
source("crosstab.R")

crosstab(bedahdata, row.vars = "namapemda", type = "frequency")


#terdapat 2 tahun anggaran 2018 dan 2019
crosstab(bedahdata, row.vars = "tahunanggaran", type = "frequency")

#subset per provinsi untuk tahun anggaran 2018
bedahdataprov2018=subset(bedahdata,tahunanggaran=="2018")
bedahdataprov2018$provtest=str_starts(bedahdataprov2018$namapemda,'Provinsi', negate=TRUE)
bedahdataprov2018=subset(bedahdataprov2018,provtest=="FALSE")

#Jumlah Frekuensi Belanja Per Provinsi Pada Tahun 2018
crosstab(bedahdataprov2018, row.vars = "namapemda", type = "frequency")
#Jumlah Frekuensi Belanja Per Fungsi Pada Tahun 2018
crosstab(bedahdataprov2018, row.vars = "namafungsi", type = "frequency")
#per nama akun jenis
crosstab(bedahdataprov2018, row.vars = "namaakunjenis", type = "frequency")
#nominal pengeluaran (terdapat negativ) 2018
pengeluaran2018perfungsi=aggregate(bedahdataprov2018$nilaianggaran, by=list(Category=bedahdataprov2018$namafungsi), FUN=sum)
#nominal pengeluaran per provinsi (terdapat negativ) 2018
pengeluaran2018perprovinsi=aggregate(bedahdataprov2018$nilaianggaran, by=list(Category=bedahdataprov2018$namapemda), FUN=sum)


#subset Pendidikan, Ekonomi, dan Kesehatan per Provinsi,
datam1=subset(bedahdataprov2018, subset = namafungsi %in% c("Ekonomi","EKONOMI","Kesehatan","KESEHATAN","Pendidikan","PENDIDIKAN"))
#efek ekonomi ke GDP Gabungkan data Ke GDP 2018
datam1eko=subset(bedahdataprov2018, subset = namafungsi %in% c("Ekonomi","EKONOMI"))

#model1 simpel eko target variable GDP mediation model (2018 training - 2019 testing, using jack knife training) , Proving the power of goverment spending in GDP
datam1ekomediationmodel=aggregate(datam1eko$nilaianggaran, by=list(Category=datam1eko$namapemda), FUN=sum)
GDP2018=GDP_perprov2018
datam1ekomediationmodel=merge(datam1ekomediationmodel,GDP2018,  by.x=c("Category"), by.y=c("Provinsi"))
datam1ekomediationmodel$GDP=as.numeric(datam1ekomediationmodel$GDP)
datam1ekomediationmodel$GDP=as.numeric(datam1ekomediationmodel$GDP)*100000
colnames(datam1ekomediationmodel)[1]  <- "Provinsi"
colnames(datam1ekomediationmodel)[2]  <- "Belanja"


#residual analisis
#---Extracting the fitted values----#
reg3$fit
#-Extracting the residuals----#
reg3$res
#---Creating a histogram of residuals---#
hist(reg3$res, main="Histogram of residual distribution from diamond ring pricing model")
#---Plotting residuals to confirm linear regression assumptions----#
par(mfrow=c(2,2))
plot(reg3)

#forecasting testing 2019
#subset per provinsi untuk tahun anggaran 2019
bedahdataprov2019=subset(bedahdata,tahunanggaran=="2019")
bedahdataprov2019$provtest=str_starts(bedahdataprov2019$namapemda,'Provinsi', negate=TRUE)
bedahdataprov2019=subset(bedahdataprov2019,provtest=="FALSE")
forecast2019=aggregate(bedahdataprov2019$nilaianggaran, by=list(Category=bedahdataprov2019$namapemda), FUN=sum)
colnames(forecast2019)[1]  <- "Provinsi"
colnames(forecast2019)[2]  <- "Belanja2019"
forecast2019=merge(forecast2019,datam1ekomediationmodel,  by.x=c("Provinsi"), by.y=c("Provinsi"))
xp=reg3$model
result=predict(reg3, newdata=xp, interval="confidence", level=.95)
result=as.data.frame(result)
result$provinsi=datam1ekomediationmodel$Provinsi
result$GDPactual=datam1ekomediationmodel$GDP
result$MODELBELANJA=datam1ekomediationmodel$Belanja
result$modelbelanjafeed=xp$Belanja
result$belanja=forecast2019$Belanja2019
forecatingresult=cbind(result$fit,result$lwr,result$upr,forecast2019$GDP)


#forecasting untuk bidang pendidikan
datam1pendi=subset(bedahdataprov2018, subset = namafungsi %in% c("Pendidikan","PENDIDIKAN"))
datam1pendi=aggregate(datam1pendi$nilaianggaran, by=list(Category=datam1pendi$namapemda), FUN=sum)
datam1pendimodel=pendidikan
regpend=lm(Index.Pembangunan.Manusia~Total.belanja.2018+Broken.Stick.1,data=datam1pendimodel)
summary(regpend)
anova(regpend)





#pemilihan data untuk dashboard
bedahdataprovdashboard=bedahdata
bedahdataprovdashboard$provtest=str_starts(bedahdataprovdashboard$namapemda,'Provinsi', negate=TRUE)
bedahdataprovdashboard=subset(bedahdataprovdashboard,provtest=="FALSE")
bedahdataprovdashboard=subset(bedahdataprovdashboard, subset = namafungsi %in% c("Ekonomi","EKONOMI","Pendidikan","PENDIDIKAN"))
bedahdataprovdashboard=aggregate(bedahdataprovdashboard$nilaianggaran, by=list(Category=bedahdataprovdashboard$namapemda,bedahdataprovdashboard$namafungsi,bedahdataprovdashboard$tahunanggaran), FUN=sum)

#make the model more stable
hist(datam1ekomediationmodel$GDP, main="Histogram of residual GDP 2018")
stabledatam1ekomediationmodel <- datam1ekomediationmodel[-c(4, 8),]

reg1=lm(GDP~Belanja,data=stabledatam1ekomediationmodel)
summary(reg1)
anova(reg1)

reg2=lm(GDP~Belanja+Reference.Level.Pemerintahan,data=stabledatam1ekomediationmodel)
summary(reg2)
anova(reg2)

reg3=lm(GDP~Belanja+Belanja*Reference.Level.Pulau,data=stabledatam1ekomediationmodel)
summary(reg3)
anova(reg3)


#boxplot
boxplot(stabledatam1ekomediationmodel$Belanja)


#simple testing of forecasting
#----Confidence and prediction intervals from Level 4----#
xp = data.frame(estress = 3,affect=1.16,ese=4.35)
#----If you want a confidence interval------#
predict(reg4, newdata=xp, interval="confidence", level=.95)
#----If you want a confidence interval------#
predict(reg4, newdata=xp, interval="prediction", level=.95)




#tahun 2018 per nama fungsi kegiatan
crosstab(bedahdata, row.vars = "namafungsi", type = "frequency")