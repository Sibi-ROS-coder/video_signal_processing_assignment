clear all;
clc;
original_video_sequence = 'football_cif.yuv';
new_video_sequence = 'qp26.yuv';
%print('Orinigal Read');
[Y1,U1,V1] = yuvRead(original_video_sequence, 352, 288,150);
%print('Ref Read');
[Y2,U2,V2] = yuvRead(new_video_sequence, 352, 288,150);

for i = 1:150
   %imshow(Y1(:,:,iFrame));
   mse(i)= sum(sum((double(Y1(:,:,i))-double(Y2(:,:,i))).^2))/(176*144);
   psnr(i)=10*log10(255^2/mse(i));
end
 %mse(i) = sum(sum((double(Y1(:,:,i))-double(Y2(:,:,i))).^2))/(176*144);
%msemean = (sum(mse)/length(mse));
mseavg=mean(mse(:));
psnravg=mean(psnr(:));
%figure(mseavg)
mseavg
psnravg
%Read YUV in MATLAB

function [y, u, v] = yuvRead(vid, width, height, nFrame)
fid = fopen(vid,'r');           % Open the video file
stream = fread(fid,'*uchar');    % Read the video file
length = 1.5 * width * height;  % Length of a single frame
y = uint8(zeros(height,   width,   nFrame));
u = uint8(zeros(height/2, width/2, nFrame));
v = uint8(zeros(height/2, width/2, nFrame));
for iFrame = 1:nFrame
    
    frame = stream((iFrame-1)*length+1:iFrame*length);
    
    % Y component of the frame
    yImage = reshape(frame(1:width*height), width, height)';
    % U component of the frame
    uImage = reshape(frame(width*height+1:1.25*width*height), width/2, height/2)';
    % V component of the frame
    vImage = reshape(frame(1.25*width*height+1:1.5*width*height), width/2, height/2)';
    
    y(:,:,iFrame) = uint8(yImage);
    u(:,:,iFrame) = uint8(uImage);
    v(:,:,iFrame) = uint8(vImage);
end



end