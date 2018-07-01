import cv2
import numpy as np
import matplotlib.pyplot as plt
from glob import glob
import os
import webget

## Our own py files
import get_url
import resize
import histogram_creater as hist

image_array_fck = ['http://footy.dk/wp-content/uploads/2017/04/20170417-184216-L-1000x656we.jpg',
                   'http://cphpost.dk/wp-content/uploads/2016/09/fck-630x390.jpg',
                   'http://footy.dk/wp-content/uploads/2017/01/fck1.jpg',
                   'http://m.indkast.dk/470/20700.jpg',
                   'http://m.indkast.dk/470/16700.jpg',
                   'https://bpsh2.hs.llnwd.net/e1/contenthub-cdn-origin/media/nordicbet/nordicbetdk_blog/FCK_vs_Lokomotiv_Moskva_i_Europa_League_2017_2018_1000.jpg',
                   'http://weszlo.com/wp-content/uploads/2017/02/1447010230_scanpix-20151108-201321-l.jpg',
                   'https://www.seoghoer.dk/sites/seoghoer.dk/files/media/article/1_80.jpg',
                   'http://fchnet.dk/wp-content/uploads/2017/01/Frederik-Bay_-FCK.jpg',
                   'http://fcsofa.dk/wp-content/uploads/2016/06/FCK-Falk.jpg',
                   'http://www.aktivaaretrundt.dk/Files/s-root/cftn/efj/current_efi.jpg',
                   'https://www.fck.dk/files/billeder/news/2012/Kris_Stadsgaard_2012_praesentation1.jpg',
                   'https://bdk.bmcdn.dk/media/cache/resolve/image_1500x/image/89/895951/19182892-dh.jpg',
                   'https://i.ytimg.com/vi/LtPLHDv3ryQ/maxresdefault.jpg',
                   'https://mobil.bold.dk/picture/490x/art113394.jpg']

image_array_bif = ['https://cdn.hummel.net/Admin/Public/GetImage.ashx?Width=500&Heigh=500&Compression=85&Crop=5&Image=/Files/Images/Perfion/9a6599a7-2763-40a2-989a-552ef1869c63.jpg',
                  'https://bdk.bmcdn.dk/media/cache/resolve/image_1500x/image/93/931225/20253812-brndby-ob-superliga-fodbold-br.jpg',
                  'http://footy.dk/wp-content/uploads/2018/04/20180408-183010-L-1000x675we.jpg',
                  'https://i.ebayimg.com/images/g/3DgAAOSwWxNYxDAR/s-l960.jpg',
                  'http://www.idealbureau.dk/wp-content/uploads/2018/01/1100x1000_team.jpg',
                  'http://footy.dk/wp-content/uploads/2017/11/20171105-130205-L-1000x665we.jpg',
                  'http://www.idealbureau.dk/wp-content/uploads/2018/01/1100x1000_team.jpg',
                  'http://hikfodbold.dk/upload/Billeder_til_artikler_/Bjorn_Kopplin%20-%20Copy%201.jpg',
                  'https://assets-jpcust.jwpsrv.com/thumbs/HqcMywpT-320.jpg',
                  'https://i.ytimg.com/vi/Idffu7BoBvM/maxresdefault.jpg',
                  'https://brondby.com/upload/biffile0_z7m7n6s3t1wzjze7btci_70126.jpg',
                  'https://bt.bmcdn.dk/media/cache/resolve/image_1240/image/73/733489/83406-brndby-if-vil-eje-brndby-hallen--.jpg',
                  'https://brondby.com/files/billeder/Fans/Fanside537-1.jpg',
                  'http://www.arnasonarkiv.dk/billeder/140px/2014/03/20140302_1564rfc-bif/180494_x6tv80.jpg',
                  'https://bt.bmcdn.dk/media/cache/resolve/image_1240/image/73/733489/83406-brndby-if-vil-eje-brndby-hallen--.jpg']

print('Downloading FCK')
get_url.download_image(image_array_fck, 'fck')
print('Downloading Brøndby')
get_url.download_image(image_array_bif, 'bif')

print('Globbing FCK')
fck_images = glob('data/fck/*.jpg')
print('Globbing Brøndby')
bif_images = glob('data/bif/*.jpg')

print('Resizes FCK')
resize.resize_image(fck_images)
print('Resizes Brøndby')
resize.resize_image(bif_images)

print('Creating histograms for FCK')
hist.histogram_saver(fck_images, 'Super FCK')
print('Creating histograms for Brøndby')   
hist.histogram_saver(bif_images, 'Super BIF')

print('One image')
hist.oneimage('Fanside537-1.jpg')
hist.oneimage('Frederik-Bay_-FCK.jpg')