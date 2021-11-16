#!/usr/bin/env python
# coding: utf-8

# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td>In [1]:</td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>In [2]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [3]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><em>"""</em><br />
# <em>Name: Liban Ali</em><br />
# <em>ID: M00520253</em><br />
# <em>Email: LA627@live.mdx.ac.uk</em><br />
# <em>"""</em><br />
# <em>"""</em><br />
# <em>Name: Rabia Irfan</em><br />
# <em>"""</em><br />
# <strong>importmatplotlib.pyplotasplt</strong><br />
# <strong>importpandasaspd</strong><br />
# <strong>importnumpyasnp</strong><br />
# <strong>fromsklearn.linear_modelimport</strong> LinearRegression <strong>fromsklearn.linear_modelimport</strong> Ridge<br />
# <strong>fromsklearn.linear_modelimport</strong> RidgeCV<br />
# <strong>fromsklearn.linear_modelimport</strong> Lasso<br />
# <strong>fromsklearn.model_selectionimport</strong> train_test_split <strong>fromsklearn.preprocessingimport</strong> StandardScaler <strong>fromsklearn.model_selectionimport</strong> KFold</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>df = pd.read_csv('Desktop/synthetic.csv')</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>print(df)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td>x1 x2 x3 x4 x5 x6</td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>\</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0 16.967792 17.299906 10.842266 15.511571 17.616665 -25.992496</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>1 16.780632 21.942175 48.655572 -3.923519 12.515563 1.189123</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>2 13.982242 10.523966 18.327122 -4.600511 5.877640 -18.146897</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>3 7.605712 17.542918 41.860639 -1.182127 17.202401 -6.528176</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>4 9.600247 12.333797 26.824897 11.596199 18.875151 -17.500930</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>.. ... ... ... ... ... ...</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>195 12.687079 12.933948 28.187807 0.977466 11.561270 -1.318645</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>196 11.357531 10.377835 24.496739 3.387472 12.987856 -8.711353</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>197 11.028283 1.890585 35.216386 -0.270869 13.039504 0.484123</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>198 9.218063 16.608357 36.119907 9.292343 10.660738 -1.907668</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>199 9.705803 15.423293 24.673363 9.380665 2.755407 1.352125</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>x7 x8 x9 x10 ... x42 x</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>43 \</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0 5.533636 18.422843 -19.352110 13.018145 ... 13.980005 -9.3986</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>01</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>1 4.291448 5.755105 -18.177523 13.842992 ... -0.510062 -6.1468</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>13</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>2 6.053160 17.263444 -18.060451 14.351065 ... 23.282090 -12.5598</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>00</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>3 4.410899 23.213193 -15.128678 16.002830 ... -2.296166 -7.8140</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>61</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>4 7.472530 18.702467 -36.212971 15.137180 ... 15.090340 -10.6282</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>51</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>.. ... ... ... ... ... ...</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>...</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>195 4.948500 19.588370 -6.723941 16.436404 ... 6.086109 -11.4656</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>02</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>196 3.250342 13.787363 -1.248170 18.084297 ... -1.639183 -3.4873</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>65</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>197 3.587833 21.854632 -32.962126 16.261560 ... 0.080211 -13.1208</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>84</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>198 5.340849 18.357629 -0.937858 11.440886 ... 1.462979 -13.0376</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>65</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>199 6.085509 22.649196 -21.530582 14.838271 ... 11.864838 -15.1331</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>28</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>x44 x45 x46 x47 x48 x49</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>\</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0 21.172492 10.183513 -21.289326 -2.780215 8.542006 12.691607</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>1 32.619986 -6.198399 -16.037733 -2.259005 0.773316 22.505565</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>2 -0.935968 14.025985 -15.404147 3.275131 7.788847 14.904073</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>3 -0.454323 9.386957 11.339227 -2.967299 11.192742 26.438028</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>4 13.898541 6.935319 21.511611 5.314873 -2.939000 9.645770</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>.. ... ... ... ... ... ...</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>195 21.323790 0.769717 16.087790 -7.966098 -31.501080 26.508728</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>196 12.816682 6.913577 -4.548838 -5.090281 -12.242855 16.750257</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>197 20.884127 12.648885 -1.840028 -2.588737 25.716845 24.092316</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>198 24.473273 21.640967 27.139826 14.664091 -2.748593 14.793366</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>199 27.308138 16.582513 26.792810 -6.699529 30.740183 19.870931</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>x50 y</td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0 -1.768255 3.379495</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>1 26.406970 -3.249131</td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>2 5.499794 -4.640679</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>3 21.693542 -4.239932</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>4 44.806762 1.745011</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>.. ... ...</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>195 -18.485878 0.850463</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>196 -17.663710 -7.424674</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>197 5.909166 -3.938403</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>198 -24.515875 0.509199</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>199 6.225972 2.773376</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>[200 rows x 51 columns]</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [5]:</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Out[5]:</p>
# </blockquote></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>x1</strong></td>
# <td><strong>x2</strong></td>
# <td><strong>x3</strong></td>
# <td><strong>x4</strong></td>
# <td><strong>x5</strong></td>
# <td><strong>x6</strong></td>
# <td><strong>x7</strong></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>count</strong></td>
# <td><blockquote>
# <p>200.000000</p>
# </blockquote></td>
# <td>200.000000</td>
# <td>200.000000</td>
# <td>200.000000</td>
# <td>200.000000</td>
# <td>200.000000</td>
# <td>200.000000</td>
# <td><blockquote>
# <p>200.0</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>mean</strong></td>
# <td><blockquote>
# <p>12.545261</p>
# </blockquote></td>
# <td><blockquote>
# <p>12.873002</p>
# </blockquote></td>
# <td><blockquote>
# <p>15.222447</p>
# </blockquote></td>
# <td>6.276543</td>
# <td><blockquote>
# <p>11.610010</p>
# </blockquote></td>
# <td><blockquote>
# <p>-4.924359</p>
# </blockquote></td>
# <td>5.182330</td>
# <td><blockquote>
# <p>16.7</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>std</strong></td>
# <td>3.012905</td>
# <td>5.933049</td>
# <td><blockquote>
# <p>19.080559</p>
# </blockquote></td>
# <td>5.559044</td>
# <td>4.990649</td>
# <td>9.438339</td>
# <td>1.625540</td>
# <td>4.0</td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>min</strong></td>
# <td>5.374438</td>
# <td><blockquote>
# <p>-4.556608</p>
# </blockquote></td>
# <td>-37.201843</td>
# <td><blockquote>
# <p>-9.449166</p>
# </blockquote></td>
# <td><blockquote>
# <p>-3.070806</p>
# </blockquote></td>
# <td>-26.252219</td>
# <td>1.702858</td>
# <td>5.7</td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>25%</strong></td>
# <td><blockquote>
# <p>10.033454</p>
# </blockquote></td>
# <td>9.150277</td>
# <td>2.963352</td>
# <td>2.577650</td>
# <td>8.406390</td>
# <td>-11.846636</td>
# <td>4.050795</td>
# <td><blockquote>
# <p>14.3</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>50%</strong></td>
# <td><blockquote>
# <p>12.248537</p>
# </blockquote></td>
# <td><blockquote>
# <p>12.929495</p>
# </blockquote></td>
# <td><blockquote>
# <p>13.840440</p>
# </blockquote></td>
# <td>6.316664</td>
# <td><blockquote>
# <p>11.164148</p>
# </blockquote></td>
# <td><blockquote>
# <p>-3.996033</p>
# </blockquote></td>
# <td>5.037758</td>
# <td><blockquote>
# <p>16.6</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>75%</strong></td>
# <td><blockquote>
# <p>14.576954</p>
# </blockquote></td>
# <td><blockquote>
# <p>16.363740</p>
# </blockquote></td>
# <td><blockquote>
# <p>29.177424</p>
# </blockquote></td>
# <td><blockquote>
# <p>10.463052</p>
# </blockquote></td>
# <td><blockquote>
# <p>15.102355</p>
# </blockquote></td>
# <td>1.891414</td>
# <td>6.270097</td>
# <td><blockquote>
# <p>19.4</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>max</strong></td>
# <td><blockquote>
# <p>21.302972</p>
# </blockquote></td>
# <td><blockquote>
# <p>32.091179</p>
# </blockquote></td>
# <td><blockquote>
# <p>63.689815</p>
# </blockquote></td>
# <td><blockquote>
# <p>18.811573</p>
# </blockquote></td>
# <td><blockquote>
# <p>25.566804</p>
# </blockquote></td>
# <td><blockquote>
# <p>20.368141</p>
# </blockquote></td>
# <td>9.377659</td>
# <td><blockquote>
# <p>27.8</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>8 rows × 51 columns</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [15]:</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>In [42]:</p>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>df.describe()</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0. 2, random_state =100)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>scaler = StandardScaler()<br />
# scaler.fit(X_train)<br />
# X_training_st = scaler.transform(X_train)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# |     |
# |-----|
# |     |
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>X_testing_st = scaler.transform(X_test) pd.DataFrame(X_training_st).describe()</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# > Out\[42\]:
# 
# <table>
# <thead>
# <tr class="header">
# <th><strong>0</strong></th>
# <th><strong>1</strong></th>
# <th><strong>2</strong></th>
# <th><strong>3</strong></th>
# <th><strong>4</strong></th>
# <th><strong>5</strong></th>
# <th></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td><strong>count</strong></td>
# <td><blockquote>
# <p>1.600000e+02</p>
# </blockquote></td>
# <td><blockquote>
# <p>1.600000e+02</p>
# </blockquote></td>
# <td><blockquote>
# <p>160.000000</p>
# </blockquote></td>
# <td>1.600000e+02</td>
# <td>1.600000e+02</td>
# <td>1.600000e+02</td>
# <td><blockquote>
# <p>1.</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>mean</strong></td>
# <td><blockquote>
# <p>-1.103284e-16</p>
# </blockquote></td>
# <td><blockquote>
# <p>1.720846e-16</p>
# </blockquote></td>
# <td>0.000000</td>
# <td>-6.730727e-17</td>
# <td>-3.668940e-17</td>
# <td><blockquote>
# <p>2.289835e-17</p>
# </blockquote></td>
# <td><blockquote>
# <p>-1</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>std</strong></td>
# <td><blockquote>
# <p>1.003140e+00</p>
# </blockquote></td>
# <td><blockquote>
# <p>1.003140e+00</p>
# </blockquote></td>
# <td>1.003140</td>
# <td>1.003140e+00</td>
# <td>1.003140e+00</td>
# <td>1.003140e+00</td>
# <td><blockquote>
# <p>1.</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>min</strong></td>
# <td><blockquote>
# <p>-2.399834e+00</p>
# </blockquote></td>
# <td><blockquote>
# <p>-2.920409e+00</p>
# </blockquote></td>
# <td>-2.893924</td>
# <td>-2.289612e+00</td>
# <td>-3.011280e+00</td>
# <td>-2.372659e+00</td>
# <td><blockquote>
# <p>-2.</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>25%</strong></td>
# <td><blockquote>
# <p>-8.214271e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>-6.277168e-01</p>
# </blockquote></td>
# <td>-0.626727</td>
# <td>-7.014355e-01</td>
# <td>-6.768465e-01</td>
# <td>-6.297981e-01</td>
# <td><blockquote>
# <p>-7</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>50%</strong></td>
# <td><blockquote>
# <p>-1.048947e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>6.064197e-03</p>
# </blockquote></td>
# <td>-0.090706</td>
# <td>-3.933537e-03</td>
# <td>-5.454037e-02</td>
# <td><blockquote>
# <p>1.058498e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>-6</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><strong>75%</strong></td>
# <td><blockquote>
# <p>6.665324e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>5.760113e-01</p>
# </blockquote></td>
# <td>0.695663</td>
# <td><blockquote>
# <p>7.538291e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>7.400409e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>7.183000e-01</p>
# </blockquote></td>
# <td><blockquote>
# <p>7</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><strong>max</strong></td>
# <td><blockquote>
# <p>2.917957e+00</p>
# </blockquote></td>
# <td><blockquote>
# <p>3.193143e+00</p>
# </blockquote></td>
# <td>2.530693</td>
# <td>2.303104e+00</td>
# <td>2.361368e+00</td>
# <td>2.891351e+00</td>
# <td><blockquote>
# <p>2.</p>
# </blockquote></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>8 rows × 50 columns</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [43]:</td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>In [19]:</p>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>scaler = StandardScaler()<br />
# scaler.fit(Y_train)<br />
# Y_training_st = scaler.transform(Y_train) Y_testing_st = scaler.transform(Y_test)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><strong>fromsklearn.model_selectionimport</strong> train_test_split<br />
# <strong>fromsklearn.model_selectionimport</strong> KFold<br />
# <strong>fromsklearn.model_selectionimport</strong> cross_val_score<br />
# <strong>fromsklearn.linear_modelimport</strong> LinearRegression<br />
# <strong>fromnumpyimport</strong> mean<br />
# <strong>fromnumpyimport</strong> absolute<br />
# <strong>fromnumpyimport</strong> sqrt<br />
# cv = KFold(n_splits =3, random_state =1, shuffle =<strong>True</strong>) model = LinearRegression()</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# |     |
# |-----|
# |     |
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>scores = cross_val_score(model, X, Y, scoring ='neg_mean_absolute_erro r', cv = cv, n_jobs =-1)<br />
# scores = cross_val_score(model, X, Y, scoring ='neg_mean_squared_erro r', cv = cv, n_jobs =-1)<br />
# print("Mean Absolute Error:", (mean(absolute(scores))))<br />
# print ("Root Mean Squared Error:", (sqrt(mean(absolute(scores)))))</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# > Mean Absolute Error: 15.955000363810717  
# > Root Mean Squared Error: 3.994371084890676
# 
# <table>
# <thead>
# <tr class="header">
# <th>In [63]:</th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>Lasso score: 0.3188137312881403</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>Lasso MSE: 7.6703108633223795</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>Lasso coef: [ 0.00000000e+00 1.08198071e-01 9.42278064e-03 0.0000000</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.00000000e+00 0.00000000e+00 -0.00000000e+00 0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00000000e+00 0.00000000e+00 0.00000000e+00 8.33054146e-02</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.00000000e+00 0.00000000e+00 -0.00000000e+00 0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00000000e+00 1.72227996e-02 -0.00000000e+00 -0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>-0.00000000e+00 2.16972458e-03 -0.00000000e+00 -1.19734488e-02</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>1.32019136e-02 0.00000000e+00 0.00000000e+00 7.72824507e-02</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>-0.00000000e+00 -6.03036797e-02 0.00000000e+00 -0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00000000e+00 0.00000000e+00 -4.34288718e-04 -0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>-0.00000000e+00 -0.00000000e+00 0.00000000e+00 9.59662545e-05</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-1.79116977e-02 4.17089787e-02 -0.00000000e+00 -8.93173265e-03</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>-0.00000000e+00 5.34597518e-03 -4.24407242e-02 -0.00000000e+00</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00000000e+00 -2.92678177e-03]</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>In [64]:</p>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td>PDFCROWD</td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><strong>fromsklearnimport</strong> linear_model<br />
# <strong>fromsklearn.metricsimport</strong> mean_squared_error<br />
# lasso = linear_model.Lasso()<br />
# lasso.fit(X,Y)<br />
# print("Lasso score:", lasso.score(X, Y))<br />
# print("Lasso MSE:", mean_squared_error(Y, lasso.predict(X))) print("Lasso coef:", lasso.coef_)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>alphas =range(1,300)<br />
# alphas = np.array(alphas)/1000<br />
# train_scores = np.array([])<br />
# test_scores = np.array([])</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><table>
# <tbody>
# <tr class="odd">
# <td>In [58]:</td>
# </tr>
# </tbody>
# </table></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><img src="attachment:08b4d0fda7a94252b443ec17d0981e55/media/image1.png" style="width:4.2in;height:2.82083in" /></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [59]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td>PDFCROWD</td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><strong>for</strong> a <strong>in</strong> alphas:<br />
# lm = Lasso(alpha = a)<br />
# lm.fit(X_train, Y_train)<br />
# train_score = lm.score(X_train, Y_train)<br />
# test_score = lm.score(X_test, Y_test)<br />
# train_scores = np.append(train_scores, train_score) test_scores = np.append(test_scores, test_score)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>plt.plot(alphas, train_scores, label ='R2 on Train', color ='red') plt.plot(alphas, test_scores, label ='R2 on Test', color ='grey') plt.xlabel('Coefficient Index', fontsize =18)<br />
# plt.ylabel('R2', fontsize =18)<br />
# plt.legend(fontsize =13, loc =4)<br />
# plt.show()</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>tunedAlphaLasso = alphas[np.argmax(train_scores)] print("tuned alpha lasso:",tunedAlphaLasso)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>tuned alpha lasso: 0.001</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>In [60]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>Lasso R2 on train 0.41334544688301744</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>Lasso R2 on test -0.00440870098959989</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [65]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [67]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Out[67]: Text(0, 0.5, '$R^2$')</p>
# </blockquote></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>print("Lasso R2 on train", train_scores[np.argmax(test_scores)]) print("Lasso R2 on test", test_scores[np.argmax(test_scores)])</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>alphas =range(0,100)<br />
# train_scores = np.array([])<br />
# test_scores = np.array([])<br />
# <strong>for</strong> a <strong>in</strong> alphas:<br />
# lm = Ridge(alpha = a)<br />
# lm.fit(X_train, Y_train)<br />
# train_score = lm.score(X_train, Y_train)<br />
# test_score = lm.score(X_test, Y_test)<br />
# train_scores = np.append(train_scores, train_score) test_scores = np.append(test_scores, test_score)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>plt.plot(alphas, train_scores, label ='R2 on Train', color ='green') plt.plot(alphas, test_scores, label ='R2 on Test', color ='purple') plt.xlabel(r'Coefficient $\alpha$', fontsize =18)<br />
# plt.ylabel(r'$R^2$', fontsize =18)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><img src="attachment:08b4d0fda7a94252b443ec17d0981e55/media/image2.png" style="width:4.22083in;height:2.82083in" /></p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>In [68]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>tuned alpha ridge: 0</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [70]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>99</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [71]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>R2 on train = 0.44042989566213064</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>R2 on test = -0.11774466914380222</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>In [74]:</p>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>tunedAlphaRidge = alphas[np.argmax(train_scores)] print("tuned alpha ridge:",tunedAlphaRidge)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>tunedAlphaRidge = alphas[np.argmax(test_scores)] print(tunedAlphaRidge)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>print("R2 on train =", train_scores[np.argmax(train_scores)]) print("R2 on test =", test_scores[np.argmax(test_scores)])</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>lm_ols = LinearRegression()<br />
# lm_ridge = Ridge(alpha = tunedAlphaRidge)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# |     |
# |-----|
# |     |
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>lm_lasso = Lasso(alpha = tunedAlphaLasso) lm_ols.fit(X_training_st, Y_training_st) lm_ridge.fit(X_training_st, Y_training_st) lm_lasso.fit(X_training_st, Y_training_st)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# > Out\[74\]: Lasso(alpha=0.001)
# 
# <table>
# <thead>
# <tr class="header">
# <th>In [76]:</th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>ols regression train score: 0.44042989566213075</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>ols regression test score: -0.14476881443400114</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>ridge regression train score: 0.3621625087932344</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>ridge regression test score: 0.05385809837780542</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>ridge regression train score: 0.4403454459099704</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>ridge regression test score: -0.13206489913525976</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [77]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Out[77]: array([[ 0.05365225, 0.27833777, 0.06010469, 0.12303554, 0.0258764</p>
# </blockquote></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>4,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.0312499 , -0.06265546, 0.0236301 , 0.06922703, 0.0089258</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.06766365, 0.26348965, 0.0423656 , 0.11544787, -0.1025093</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>9,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00804577, 0.04599939, 0.06322446, -0.08810868, -0.0010083</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td>PDFCROWD</td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>ols_train_score = lm_ols.score(X_training_st, Y_training_st) ols_test_score = lm_ols.score(X_testing_st, Y_testing_st)<br />
# ridge_train_score = lm_ridge.score(X_training_st, Y_training_st) ridge_test_score = lm_ridge.score(X_testing_st, Y_testing_st) lasso_train_score = lm_lasso.score(X_training_st, Y_training_st) lasso_test_score100 = lm_lasso.score(X_testing_st, Y_testing_st) print("ols regression train score:", ols_train_score)<br />
# print("ols regression test score:", ols_test_score)<br />
# print("ridge regression train score:", ridge_train_score)<br />
# print("ridge regression test score:", ridge_test_score)<br />
# print("ridge regression train score:", lasso_train_score)<br />
# print("ridge regression test score:", lasso_test_score100)</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>lm_ols.coef_</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>5,</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>-0.08396093, 0.07676675, -0.01177237, -0.09303901, 0.1333658</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>8,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.02872996, -0.07236306, 0.22434912, -0.12318932, -0.2482271</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>3,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.03983445, 0.00281999, 0.03325123, 0.02726317, -0.0748475</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>6,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.065056 , -0.07351037, 0.03171876, 0.11899895, -0.0031575</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>2,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>-0.07165325, 0.22293061, 0.01699175, -0.11024534, -0.0561969</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>3,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.02216296, -0.16548784, -0.09170411, 0.0085432 , -0.1002807</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>5]])</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [78]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Out[78]: array([[ 0.0011118 , 0.15565109, 0.04165444, 0.05455839, -0.0021467</p>
# </blockquote></td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>8,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.02291474, -0.01998058, 0.00434212, 0.01698587, 0.0059878</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>1,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.03491743, 0.15681698, 0.03790501, 0.0468312 , -0.0436664</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>4,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.01681556, 0.01942569, 0.03687335, -0.04935627, -0.0186647</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-0.02252138, 0.04711715, -0.0131801 , -0.04861951, 0.0921295</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>9,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.01527396, -0.02426917, 0.12495428, -0.06162043, -0.1299000</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>7,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.027041 , 0.00817355, 0.02915675, 0.00230723, -0.0445139</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>7,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.00472135, -0.03059412, 0.01172883, 0.058157 , 0.0257554</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>2,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-0.03500732, 0.09086811, 0.00567934, -0.06953108, -0.0414910</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>9,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-0.00896513, -0.10664159, -0.06172448, -0.02184334, -0.0276725</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>8]])</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>In [79]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>lm_ridge.coef_</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>lm_lasso.coef_</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>Out[79]: array([ 0.05087254, 0.27692376, 0.05931901, 0.12020492, 0.02380196,</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td>0.02959725, -0.06088904, 0.02185944, 0.06653258, 0.00783868,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.06585205, 0.26201764, 0.04190092, 0.11296589, -0.10064479,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.00668761, 0.043851 , 0.0625498 , -0.08670438, -0.00123325,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-0.08179591, 0.07560293, -0.01091182, -0.09147531, 0.13069936,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.02710831, -0.06978337, 0.22398388, -0.12077464, -0.24501388,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>0.03864725, 0.00211118, 0.03347204, 0.02535204, -0.07323794,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.06252473, -0.07179028, 0.02972178, 0.11658283, -0.00050126,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>-0.07063756, 0.21969805, 0.0156507 , -0.10855949, -0.0556655 ,</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>0.02060364, -0.16512953, -0.08979873, 0.00589066, -0.0975283</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td>])</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="odd">
# <td>In [82]:</td>
# <td></td>
# <td></td>
# </tr>
# <tr class="even">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# <td></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>x_axis = np.array(range(0, len(lm_ols.coef_.ravel())))<br />
# y_ols =abs(lm_ols.coef_.ravel())<br />
# y_ridge =abs(lm_ridge.coef_.ravel())<br />
# y_lasso =abs(lm_lasso.coef_.ravel())<br />
# plt.plot(x_axis, y_ols, alpha=1, linestyle='none', marker='*', markersi ze=5, color='red', label="OLS")<br />
# plt.plot(x_axis, y_ridge, alpha=0.5, linestyle='none', marker='d', mark ersize=6, color='blue', label="Ridge")<br />
# plt.plot(x_axis, y_lasso, alpha=0.25, linestyle='none', marker='o', mar kersize=7, color='green', label="Lasso")<br />
# plt.xlabel('Coefficient Index', fontsize=14)<br />
# plt.ylabel('Absolute Coefficient Magnitude', fontsize=14)<br />
# plt.legend(fontsize=10, loc=4)<br />
# plt.show()</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
# 
# <table>
# <thead>
# <tr class="header">
# <th><table>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p><img src="attachment:08b4d0fda7a94252b443ec17d0981e55/media/image3.png" style="width:4.1375in;height:2.8in" /></p>
# </blockquote></td>
# </tr>
# </tbody>
# </table></th>
# <th></th>
# </tr>
# </thead>
# <tbody>
# <tr class="odd">
# <td><blockquote>
# <p>Create PDF in your applications with the Pdfcrowd HTML to PDF API</p>
# </blockquote></td>
# <td><blockquote>
# <p>PDFCROWD</p>
# </blockquote></td>
# </tr>
# </tbody>
# </table>
