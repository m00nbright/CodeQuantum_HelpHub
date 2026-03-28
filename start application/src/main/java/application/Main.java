package application;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.text.Font;
import javafx.event.ActionEvent;
import javafx.scene.control.Label;
import javafc.scene.layout.VBox;
import javafx.scene.layout.*




public class Main extends Application {
    Label lblHomeTitle = new Label("Welcome to Help Hub!");

    @Override
    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws IOException {

        VBox vbHomePage = new VBox(10, lblHomeTitle);
        vbHomePage.setAlignment(Pos.CENTER);

        Scene scene = new Scene(new StackPane(), 400, 300);
        stage.setTitle("Help Hub");
        stage.setScene(scene);
        stage.show();

            
    }
}