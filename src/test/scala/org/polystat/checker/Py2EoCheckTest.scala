package org.polystat.checker

import org.junit.jupiter.api.Test

import scala.reflect.io.Directory
import scala.sys.process.Process

final class Py2EoCheckTest {

  private val py2eoLink = "https://github.com/polystat/py2eo"

  @Test def py2EoCheck(): Unit = {
    val directory = Directory.makeTemp(prefix = "org.polystat.checker.")
    val py2eo = Directory(directory / "py2eo")

    Process(s"git clone $py2eoLink ${py2eo.name}", directory.jfile).!!

    val input = Directory(py2eo / "transpiler/src/test/resources/org/polystat/py2eo/transpiler/simple-tests")
    val output = Directory(directory / "output").createDirectory()

    Check(input, output)
    directory.deleteRecursively
  }
}
