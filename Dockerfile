FROM bitnami/git

WORKDIR /holberton/github/holbertonschool-higher_level_programming
COPY . .
RUN chmod +rx entrypoint.sh
RUN git config --global user.name "jesus"
RUN git config --global user.email "jesusmanuel.maciasmartinez@gmail.com"
RUN git config --global --add safe.directory /holberton/github/holbertonschool-higher_level_programming
#RUN git init
#RUN git remote add origin https://github.com/Ragnar9902/holbertonschool-higher_level_programming.git
RUN git branch -M master


#ENTRYPOINT ["sh", "entrypoint.sh"]