  data = sub.readall.Data;
    x = zeros(size(data,1),1);
    y = zeros(size(data,1),1);
    z = zeros(size(data,1),1);
    for i= 1:size(data, 1)
        chardata = char(data(i, :));
        x(i) = str2double(chardata(1:7));
        y(i) = str2double(chardata(9:16));
        z(i) = str2double(chardata(18:25));
        if x(i)^2 + y(i)^2 + z(i)^2 < 1 || x(i)^2 + y(i)^2 + z(i)^2 > 300^2
            x(i) = NaN;
            y(i) = NaN;
            z(i) = NaN;
        end
    end
    plot3(x, y, z, 'o')